import pandas as pd

df1 = pd.DataFrame({'Roll No.': [1,2,3,4,5], 'Maths':[45,78,45,90,66], 'Physics': [33,67,12,90,44]})
df2 = pd.DataFrame({'Roll No.': [6,7,8,9,10], 'Maths': [78,73,45,90, 69], 'Physics': [23, 67, 88, 0, 98]})
print(df1)
print(df2)
print("\n================================")

print(df1._append(df2))
print("\n================================")

print(df1._append(df2, ignore_index=True))
print("\n================================")

print(df1._append(df2, ignore_index=True, sort=True))
print("\n================================")


df1 = pd.DataFrame({'Roll No.': [1,2,3,4,5], 'Chemistry':[45, 78, 45, 90, 66],'Physics': [33,67,12,90,44]})
df2 = pd.DataFrame({'Roll No.': [6,7,8,9,10], 'Maths': [78,73,45,90, 69], 'Physics': [23, 67, 88, 0, 98]})
print(df1)
print(df2)
print("\n=====================================")

print(df1._append(df2, ignore_index=True))
print("\n=========================")

df1 = pd.DataFrame({'Roll No.': [1,2,3,4,5], 'Maths':[45,78,45,90,66], 'Chemistry':[45, 78, 45, 90, 66],'Physics': [33,67,12,90,44]})
df2 = pd.DataFrame({'Roll No.': [6,7,8,9,10], 'Maths': [78,73,45,90, 69], 'Physics': [23, 67, 88, 0, 98]})
print(df1)
print("\n=====================================")
print(df2)
print("\n=====================================")

print(df1._append(df2, ignore_index=True))
