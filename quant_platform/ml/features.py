import pandas as pd

def create_lag_features(df: pd.DataFrame, columns: list, lags: int = 3) -> pd.DataFrame:
    # Generate lagged features for specific columns.
    for col in columns:
        for lag in range(1, lags + 1):
            df[f"{col}_{lag}"] = df[col].shift(lag)
    return df