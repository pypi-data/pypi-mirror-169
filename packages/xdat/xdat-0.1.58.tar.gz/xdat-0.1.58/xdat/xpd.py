from collections import Counter
import fnmatch

from caseconverter import snakecase
import pandas
import numpy as np
import pandas as pd
from slugify import slugify

from . import xsettings
from . import xagg


def x_gen_grouped_counter(df, group_on=None, sort_on=None, start=0):
    if sort_on:
        df = df.sort_values(sort_on)

    return df.groupby(group_on).cumcount() + start


def x_iter_groups(df, on):
    if not on:
        yield df, [], ""
        return

    if isinstance(on, str):
        on = [on]

    df = df.sort_values(on)
    groups = df.groupby(on)
    for group_keys, df_group in groups:
        if not isinstance(group_keys, list) and not isinstance(group_keys, tuple):
            group_keys = [group_keys]

        group_title = ", ".join([f"{k}={v}" for k,v in zip(on, group_keys)])
        yield df_group, group_keys, group_title


def x_merge(df_self, right, x_drop_dup_cols=True, drop_diff_cols=False, log=None, **kwargs):
    """
    A wrapper around pd.merge().
    Gets rid of as many duplicate columns ('_x', '_y') as possible after the merge.
    """
    
    df = df_self.merge(right, **kwargs)

    if log:
        on = kwargs['on']
        kleft = df_self[on].drop_duplicates()
        kright = right[on].drop_duplicates()
        kleft['xleft'] = 1
        kright['xright'] = 1

        both = kleft.merge(kright, on=on, how='outer')
        both[['xleft', 'xright']] = both[['xleft', 'xright']].fillna(0)
        both = both.sort_values(on)
        left_only = both[(both.xleft == 1) & (both.xright == 0)]
        if len(left_only):
            left_only.to_csv(xsettings.OUTPUT_PATH.joinpath(f"{log}-left_only.csv"), index=False)
        right_only = both[(both.xleft == 0) & (both.xright == 1)]
        if len(right_only):
            right_only.to_csv(xsettings.OUTPUT_PATH.joinpath(f"{log}-right_only.csv"), index=False)

    if not x_drop_dup_cols:
        return df

    suffixes = kwargs.get('suffixes', ('_x', '_y'))
    s1, s2 = suffixes
    for col1 in sorted(df.columns):
        if col1.endswith(s1):
            col_new = col1[:-1*len(s1)]
            col2 = col_new + s2

            if col_new in df.columns:
                continue

            if col2 not in df.columns:
                continue

            c1 = df[col1]
            c2 = df[col2]

            # remove if columns are exact duplicates
            if (c1 != c2).sum() == 0:
                df.rename(columns={col1: col_new}, inplace=True)
                del df[col2]
                continue

            # see if the differences are when one column is NA and the other is not
            # (can happen on a left-join, for example)
            c1b = np.where(c1.isna(), c2, c1)
            c2b = np.where(c2.isna(), c1, c2)

            if (c1b != c2b).sum() == 0:
                del df[col1]
                del df[col2]
                df[col_new] = c1b
                continue

            if drop_diff_cols:
                del df[col1]
                del df[col2]
                continue

    return df


def x_match(self, values, exclude=False):
    """
    Filter DataFrame by column values

    Examples:
    >> df['animal'].x_match(['cat', 'dog', '*ouse'], exclude=True)
    """

    possible_values = self.unique()

    if isinstance(values, str):
        values = [values]

    keep_exact = []
    for keep_pattern in values:
        if isinstance(keep_pattern, str):
            vals = [v for v in possible_values if fnmatch.fnmatch(v, keep_pattern)]
            keep_exact.extend(vals)

        else:
            keep_exact.append(keep_pattern)

    idxs = self.isin(keep_exact)
    if exclude:
        idxs = ~idxs

    return idxs


def x_filter_by(self, values, col_name, exclude=False, dropna=True, ignore_index=None, sanity_checks=None):
    """
    Filter DataFrame by column values

    Examples:
    >> df.x_filter_by(['cat', 'dog', '*ouse'], 'animal', exclude=True)
    """

    ignore_index = xsettings.get_default(xsettings.IGNORE_INDEX, ignore_index)
    sanity_checks = xsettings.get_default(xsettings.SANITY_CHECKS, sanity_checks)

    if dropna:
        self = self.dropna(subset=[col_name])

    idxs = x_match(self[col_name], values, exclude=exclude)

    df_filtered = self[idxs]

    if ignore_index:
        df_filtered = df_filtered.reset_index(drop=True)

    if sanity_checks:
        assert len(df_filtered) > 0, f"attr_name={col_name}, keep_values={values}, exclude={exclude}"

    return df_filtered


def x_split_on(self, values, col_name, ignore_index=None, drop_key_col=False):
    """
    Filters & splits dataframe by values

    >> df_cats, df_dogs = df.x_split_on(['cat', 'dog'], 'animal')
    """
    ignore_index = xsettings.get_default(xsettings.IGNORE_INDEX, ignore_index)

    res = []
    for value in values:
        df_value = x_filter_by(self, [value], col_name, ignore_index=ignore_index)
        if drop_key_col:
            del df_value[col_name]

        res.append(df_value)

    return tuple(res)


def x_append(self, other, ignore_index=None, verify_integrity=False, sort=False):
    ignore_index = xsettings.get_default(xsettings.IGNORE_INDEX, ignore_index)

    if self is None:
        return other

    if other is None:
        return self

    return self.append(other, ignore_index=ignore_index, verify_integrity=verify_integrity, sort=sort)


def x_replace(self, valid_vals=tuple(), replace_vals=None, default=None):
    replace_vals = replace_vals or dict()
    valid_vals = tuple(set(valid_vals) | set(replace_vals.keys()) | set(replace_vals.values()))

    def do(x):
        if x not in valid_vals:
            return default

        return replace_vals.get(x, x)

    sa_replaced = self.apply(do)
    return sa_replaced


def x_clean_text(self):
    return self.apply(lambda x: slugify(x, separator="_"))


def x_as_float(self, nan_texts=None):
    nan_texts = xsettings.get_default(xsettings.NAN_TEXTS, nan_texts)

    def conv(x):
        try:
            return np.float(x)
        except ValueError:
            if x.strip() in nan_texts:
                return np.nan
            raise ValueError(x)

    return self.apply(conv)


def x_apply_on_group(df, by, func):
    def wrapper(dfx):
        res = func(dfx)
        return res

    g = df.groupby(by)
    df_res = g.apply(wrapper)
    return df_res


def x_groupby(self, by, aggs, ignore_index=None, **kwargs):
    """
    A simpler groupby interface
    (inspired by Turicreate)

    >> df.x_groupby('a', {'min_b': xagg.Min('b'), 'max_c': xagg.Max('c'), 'n': xagg.Count()})
    """

    ignore_index = xsettings.get_default(xsettings.IGNORE_INDEX, ignore_index)

    d = dict()
    for k, v in aggs.items():
        if isinstance(v, xagg._Agg):
            tup = v.as_tuple()
            if tup[0] is None:
                tup = tuple([self.columns[0], tup[1]])
            d[k] = tup

        elif isinstance(v, tuple):
            d[k] = v

        else:
            raise ValueError(f"{k}: {v}")

    g = self.groupby(by=by, **kwargs).agg(**d)

    if ignore_index:
        g = g.reset_index()

    return g


def x_calc_rank_num(self, key_col_name, score_col_name, ascending=True):
    """
    creates a series ranking each group of key_col_name by score_col_name

    >> df.x_calc_rank_num('user_id', 'product_score', ascending=False)
    """

    return self.groupby(key_col_name)[score_col_name].rank(ascending=ascending).astype(int)


def x_add_history(self, key, value):
    if not hasattr(self, '_x_history'):
        self._metadata.append('_x_history')
        self._x_history = []

    self._x_history.append((key, value))


def x_get_history(self):
    if not hasattr(self, '_x_history'):
        return []

    return self._x_history


def x_set_data_type(self, data_type):
    """
    sets logical data type: binary, nominal, ordinal, interval, ratio, temporal, geojson
    (inspired by altair, etc.)
    what about cyclical? (can be either ordinal [day of week] or interval [hour of day]
    """

    if not hasattr(self, '_x_data_type'):
        self._metadata.append('_x_data_type')

    data_type = data_type.lower()[0]
    data_type = {
        'b': 'binary',
        'n': 'nominal',
        'o': 'ordinal',
        'i': 'interval',
        'r': 'ratio',
        'q': 'ratio',
        't': 'temporal',
        'g': 'geojson'
    }[data_type]

    self._x_data_type = data_type


def x_get_data_type(self):
    if not hasattr(self, '_x_data_type'):
        return None

    return self._x_data_type


def x_set_column_type(self, column_type):
    """
    sets logical column type: target, feature, meta, key
    - a target variable
    - a feature (can be used for training)
    - meta data (not to use as a training feature, but might be confounding)
    - a sample key (should be unique)
    """

    if not hasattr(self, '_x_column_type'):
        self._metadata.append('_x_column_type')

    column_type = column_type.lower()[0]
    column_type = {
        't': 'target',
        'f': 'feature',
        'm': 'meta',
        'k': 'key'
    }[column_type]

    self._x_column_type = column_type


def x_get_column_type(self):
    if not hasattr(self, '_x_column_type'):
        return None

    return self._x_column_type


def x_rename(self, mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='raise'):
    if columns is not None:
        for name_from, name_to in columns.items():
            xsettings.x_add_desc(name_to, name_from)

    self_orig = self
    self = self.rename(mapper=mapper, index=index, columns=columns, axis=axis, copy=copy, inplace=inplace, level=level, errors=errors)

    self = self if self is not None else self_orig
    return self


def x_sort_on_lookup(self: pd.DataFrame, on, sa_lookup: pd.Series, ascending=True):
    """
    Given lookup Series, merge it based 'on', and then sort, and remove
    df.x_sort_on_lookup('height', df.groupby('height')['width'].mean())
    """
    df = self.copy()
    df['tmp_x_sort_on_lookup'] = df.apply(lambda r: sa_lookup[r[on]], axis=1)
    df = df.sort_values('tmp_x_sort_on_lookup', ascending=ascending)
    del df['tmp_x_sort_on_lookup']
    return df


def x_clean_column_names(self, inplace=False, remove_parens="auto"):
    """
    renames columns to pythonable names, " Hi there" --> "hi_there"
    """

    orig_columns = self.columns
    new_columns = orig_columns[:]
    if remove_parens:
        new_columns = [c.split('(')[0] for c in new_columns]
        new_columns = [c.split('[')[0] for c in new_columns]

    new_columns = np.array([snakecase(c) for c in new_columns])

    a = pd.Series(new_columns)
    counts = a.value_counts()
    counts = counts[counts > 1]
    bad_keys = counts.index.values

    new_columns = np.where(~np.isin(new_columns, bad_keys), new_columns, np.array([slugify(c, separator='_') for c in orig_columns]))

    a = pd.Series(new_columns)
    counts = a.value_counts()

    used_counts = Counter()

    def get_new_name(col):
        if counts[col] == 1:
            return col

        used_counts[col] += 1
        c = used_counts[col]
        return f"{col}_{c}"

    new2 = [get_new_name(c) for c in new_columns]
    assert len(set(new2)) == len(orig_columns), "not all column names become unique"

    rename_dict = dict(zip(orig_columns, new2))
    return x_rename(self, columns=rename_dict, inplace=inplace)


def x_apply_multi(self):
    # TODO: do
    return self


def x_drop_by_counts(self, count_on, keep_count=None, min_count=None, max_count=None):
    """
    count number of unique values for `count_on`, and filter df by `keep_count`
    """

    sa_counts = self[count_on].value_counts()
    if keep_count:
        sa_counts = sa_counts[sa_counts == keep_count]
    if min_count:
        sa_counts = sa_counts[sa_counts >= min_count]
    if max_count:
        sa_counts = sa_counts[sa_counts <= min_count]

    self = x_filter_by(self, sa_counts.index.values, count_on)
    return self


def x_timedelta_as_hours(self):
    """
    Given a Series containing Timedelta, converts it to Series containing hours (float)
    """
    return self.apply(lambda d: d.days * 24 + d.seconds / (60 * 60))


def x_add_uid(self, on, new_col, start_with=1, sort=True):
    """
    Given a df, converts to unique IDs
    """
    if isinstance(on, str):
        on = [on]

    df = self.copy()
    new_col_temp = None
    if new_col in df.columns:
        new_col_temp = f"{new_col}__tmp"
        df.rename(columns={new_col: new_col_temp}, inplace=True)

        if new_col in on:
            on.remove(new_col)
            on.append(new_col_temp)

    df2 = df[on]
    df2 = df2.drop_duplicates()
    if sort:
        df2 = df2.sort_values(on)

    df2 = df2.reset_index(drop=True)
    df2 = df2.reset_index()
    df2.rename(columns={'index': new_col}, inplace=True)
    df2[new_col] = df2[new_col] + start_with
    df_new = df.merge(df2, on=on)

    if new_col_temp:
        del df_new[new_col_temp]

    return df_new


def x_undo_dummies(df, prefix_sep="_"):
    """
    Given df with dummy columns (created using pd.get_dummies()), undo the dummies
    Credits: https://newbedev.com/reverse-a-get-dummies-encoding-in-pandas
    """
    cols2collapse = {
        item.split(prefix_sep)[0]: (prefix_sep in item) for item in df.columns
    }
    series_list = []
    for col, needs_to_collapse in cols2collapse.items():
        if needs_to_collapse:
            undummified = (
                df.filter(like=col)
                .idxmax(axis=1)
                .apply(lambda x: x.split(prefix_sep, maxsplit=1)[1])
                .rename(col)
            )
            series_list.append(undummified)
        else:
            series_list.append(df[col])
    undummified_df = pd.concat(series_list, axis=1)
    return undummified_df


def monkey_patch():
    pandas.Series.x_match = x_match
    pandas.Series.x_replace = x_replace
    pandas.Series.x_clean_text = x_clean_text
    pandas.Series.x_add_history = x_add_history
    pandas.Series.x_get_history = x_get_history
    pandas.Series.x_set_data_type = x_set_data_type
    pandas.Series.x_get_data_type = x_get_data_type
    pandas.Series.x_set_column_type = x_set_column_type
    pandas.Series.x_get_column_type = x_get_column_type
    pandas.Series.x_as_hours = x_timedelta_as_hours

    pandas.DataFrame.x_filter_by = x_filter_by
    pandas.DataFrame.x_split_on = x_split_on
    pandas.DataFrame.x_append = x_append
    pandas.DataFrame.x_groupby = x_groupby
    pandas.DataFrame.x_calc_rank_num = x_calc_rank_num
    pandas.DataFrame.x_add_history = x_add_history
    pandas.DataFrame.x_get_history = x_get_history
    pandas.DataFrame.x_clean_column_names = x_clean_column_names
    pandas.DataFrame.x_rename = x_rename
    pandas.DataFrame.x_sort_on_lookup = x_sort_on_lookup
    pandas.DataFrame.x_undo_dummies = x_undo_dummies




