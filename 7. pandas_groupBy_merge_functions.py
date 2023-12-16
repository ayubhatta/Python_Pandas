import pandas as pd

# groupby()

df = pd.read_csv(r'C:\Users\bhatt\Downloads\sample2.csv')
print(df.head())
print("\n==========================================")

branch_group = df.groupby(by = 'Branch')
print(branch_group.groups)
print("\n==========================================")

branch_group = df.groupby(by = ['Branch', 'Section'])
print(branch_group.groups)
print("\n==========================================")

for group, data_frame in branch_group:
    print(group)
    print(data_frame)
print("\n==========================================")



# merge()

df1 = pd.DataFrame({'Roll No.': [1,2,3,4,5], 'Chemistry': [78,33,39,81,90]})
print(df1)
print("\n==========================================")

df2 = pd.DataFrame({'Roll No.': [1,2,3,4,5], 'Physics': [34,67,34, 89, 12]})
print(df2)
print("\n==========================================")

print(pd.merge(df2, df1, on = 'Roll No.'))
print("\n==========================================")

print(pd.merge(df2, df1))     # on - by default intersection column is taken
print("\n==========================================")

df3 = pd.DataFrame({'Roll No.': [1,2,3,4,5], 'Physics': [34,67,34,89,12]})
df4 = pd.DataFrame({'Roll No.': [1,2,3,8,9], 'Chemistry': [34,67,34,89,12]})
print(df3)
print("\n==========================================")

print(pd.merge(df3, df4))
print("\n==========================================")

print(pd.merge(df3, df4, how = 'left'))
print("\n==========================================")

print(pd.merge(df3, df4, how = 'right'))
print("\n==========================================")

