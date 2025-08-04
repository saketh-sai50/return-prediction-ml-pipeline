import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/cleaned_returns.csv")

print(df.describe())
sns.countplot(x='is_return', data=df)
plt.savefig("../notebooks/countplot_is_return.png")
