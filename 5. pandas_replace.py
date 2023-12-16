import pandas as pd

df = pd.read_csv(r'C:\Users\bhatt\Downloads\sample.csv')
print(df.head())
print("\n")

print(df.replace(to_replace = 26, value = 30))
print("\n")

print(df.replace(34, 1000))
print("\n")

print(df.replace(to_replace = [50,51,52,53,54,55,56,57,58,59], value = 'A'))
print("\n")

print(df.replace(to_replace = [50,51,52,53], value = ['A', 'B', 'C', 'D']))
print("\n")

df['Physics'].replace(to_replace = [50,51,52,53], value = ['A', 'B', 'C', 'D'], inplace = True)
print(df)
print("\n")

print(df.replace('[A-Za-z]', 0))
print("\n")

print(df.replace('[A-Za-z]', 0, regex = True))
print("\n")

print(df.replace(to_replace = 15, method = 'ffill'))
print("\n")

print(df.replace(to_replace = 15, method = 'bfill'))
print("\n")

