import pandas as pd

df = pd.read_csv(r"C:\Users\bhatt\Downloads\sample2.csv")
print(df.head())
print("\n================================")

print(pd.pivot_table(df, index='Branch', aggfunc='sum'))
print("\n================================")

print(pd.pivot_table(df, index='Branch', aggfunc='count'))
print("\n================================")

print(pd.pivot_table(df, index='Branch', aggfunc='max'))
print("\n================================")

print(pd.pivot_table(df, index='Branch', aggfunc='max', columns='Section'))
print("\n================================")