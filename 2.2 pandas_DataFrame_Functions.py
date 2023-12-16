# importing pandas as pd
import pandas as pd

df = pd.read_csv(r'C:\Users\bhatt\Downloads\Salary_Data.csv')    # reading csv file from my pc
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

