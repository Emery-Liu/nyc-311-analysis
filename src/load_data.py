import pandas as pd

# Purpose: Reads a CSV file from the given path and returns a pandas DataFrame
# Parameter: filepath is a string of path to the CSV
# Return: a pd.DataFrame
def load_data(filepath):
    return pd.read_csv(filepath)

