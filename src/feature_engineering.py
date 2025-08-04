import pandas as pd

def engineer_features(df):
    # Example: Encoding categorical variables
    df = pd.get_dummies(df, columns=['product_category', 'customer_region'])
    df['order_month'] = pd.to_datetime(df['order_date']).dt.month
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/cleaned_returns.csv")
    df_fe = engineer_features(df)
    df_fe.to_csv("../data/processed/returns_features.csv", index=False)
