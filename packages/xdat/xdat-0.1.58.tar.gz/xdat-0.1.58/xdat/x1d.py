import pandas as pd
from scipy import signal
from tqdm import tqdm


def array_col_to_wide(df, array_col, prefix=None):
    if prefix is None:
        prefix = f"{array_col}"

    all_rows = []
    for _, row in tqdm(df.iterrows(), total=len(df)):
        a = row[array_col]
        del row[array_col]
        for idx, v in enumerate(a):
            row[f"{prefix}_{idx}"] = v
        all_rows.append(row)

    df_all = pd.DataFrame(all_rows)
    return df_all
