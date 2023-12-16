import pandas as pd

df = pd.read_csv(r'C:\Users\bhatt\Downloads\Salary_Data.csv')
print(df.columns)

print(df.shape)

print(df.size)

print(df.head())

print(df.head(2))

print(df.tail())

print(df.tail(8))

print(df.describe())

print(df.info())

print("\n")

