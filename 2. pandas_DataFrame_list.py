# importing pandas as pd
import pandas as pd

df = pd.DataFrame()
print(df)
print("\n")

lst = [1,2,3,4,5]
df = pd.DataFrame(lst)
print(df)
print("\n")

lst = [[1,2,3,4,5], [11,12,13,14,15]]
df = pd.DataFrame(lst)
print(df)
print("\n")

a = [{'a':5, 'b':7, 'c':9, 'd':2},
      {'a':4, 'b':8, 'c':19, 'd':12}]     # Dict keys represents column names


df = pd.DataFrame(a)
print(df)
print("\n")


b = {'RollNo.': pd.Series([1,2,3,4,5]),
     'Maths': pd.Series([67,89,23,90,56]),
     'Physics': pd.Series([12,98,44,90,78])}

df = pd.DataFrame(b)
print(df)
print("\n")


