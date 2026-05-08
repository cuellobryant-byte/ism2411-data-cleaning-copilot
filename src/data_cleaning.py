import pandas as pd


def load_data(file_path: str):

    try:
        df = pd.read_csv(file_path)
        print("Raw dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
def clean_column_names(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df
