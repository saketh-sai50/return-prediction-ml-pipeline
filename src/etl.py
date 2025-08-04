import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Example cleaning
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = load_data("../data/raw/returns.csv")
    df_clean = clean_data(df)
    df_clean.to_csv("../data/processed/cleaned_returns.csv", index=False)
