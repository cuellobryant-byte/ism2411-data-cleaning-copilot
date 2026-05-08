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
def handle_missing_values(df):

    if "prodname" in df.columns:
        df["prodname"] = df["prodname"].astype(str).str.strip()

    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip()

    if "price" in df.columns:
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["price"] = df["price"].fillna(df["price"].mean())

    if "qty" in df.columns:
        df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
        df["qty"] = df["qty"].fillna(0)

    return df
def remove_invalid_rows(df):

    if "price" in df.columns:
        df = df[df["price"] >= 0]

    if "qty" in df.columns:
        df = df[df["qty"] >= 0]

    return df
if __name__ == "__main__":

    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)

    if df_raw is not None:

        df_clean = clean_column_names(df_raw)
        df_clean = handle_missing_values(df_clean)
        df_clean = remove_invalid_rows(df_clean)

        df_clean.to_csv(cleaned_path, index=False)

        print(df_clean.head())
