import pandas as pd

# pd.set_option('display.max_columns', None)
data=pd.read_csv("train.csv")
# print(data.head(15))
# print(data.describe())

# print(data.columns[data.isna().any()].tolist())
# print(data.columns.tolist())

print(data.isna().any())