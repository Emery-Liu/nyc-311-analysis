import numpy as np
import pandas as pd

HOUR_IN_SEC = 3600

# Purpose: Convert created_date(str) and closed_date(str) into datetime type,
#   add resolution_time and resolution_hours by calculate the difference between
#   created_date and closed_date
# Parameter: ori_dataframe (pd.DataFrame)
# Return: new pd.DataFrame with addtional columns
# Note: ori_dataframe must contain created_date and closed_date columns
def add_resolution_col(ori_dataframe):

    df = ori_dataframe.copy()

    df["created_date"] = pd.to_datetime(df["created_date"])
    df["closed_date"] = pd.to_datetime(df["closed_date"])

    df["resolution_time"] = df["closed_date"] - df["created_date"]

    df["resolution_hours"] = (
        df["resolution_time"]
        .dt.total_seconds()
        / HOUR_IN_SEC 
    )

    return df
