import pandas as pd

'''     Finding the Null Values     '''

df = pd.read_csv(r'C:\Users\bhatt\Downloads\sample.csv')
print(df.head())
print("\n===================================================")

print(df.isnull().sum())
print("\n===================================================")

print(df.fillna(0))  # fills the null values with 0.
print("\n===================================================")

print(df.fillna(1)) # fills the null values with 1.
print("\n===================================================")

print(df.fillna({'Physics': 'none', "Chemistry": 0, "Maths": 30}))
print("\n===================================================")

print(df.fillna(method = 'ffill'))  # ffill = forward fill, fills the missing value from its upper cell.
print("\n===================================================")

print(df.fillna(method = 'ffill', axis = 1))  # axis = 1 means the null values will be filled by the same value at its left cell.
print("\n===================================================")

print(df['Physics'].fillna(value=df['Physics'].mean()))  # mean(), in the place of null values, it fills the null values with the mean value of all the values in the row.
print("\n===================================================")

print(df.fillna(method = 'bfill'))  # backward fill, fills the missing values from its lower cell.
print("\n===================================================")

df.fillna(method = 'bfill', inplace = True)
print(df)
print("\n===================================================")

