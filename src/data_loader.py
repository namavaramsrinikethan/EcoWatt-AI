"""
data_loader.py

This module is responsible for loading datasets used by EcoWatt AI.

It supports:
1. Built-in household electricity dataset
2. User uploaded CSV files
"""

import pandas as pd
import os


def load_dataset(file_path):
    """
    Load the built-in household electricity dataset.

    Parameters:
        file_path (str): Path to dataset file.

    Returns:
        pandas.DataFrame
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    df = pd.read_csv(
        file_path,
        sep=";",
        low_memory=False,
        na_values="?"
    )

    return df

    
def display_dataset_info(df):
    """
    Display basic dataset information.

    Parameters:
        df (DataFrame)

    Returns:
        dict
    """

    info = {
    "Rows": df.shape[0],
    "Columns": df.shape[1],
    "Missing Values": int(df.isnull().sum().sum()),
    "Column Names": list(df.columns)
    }

    return info