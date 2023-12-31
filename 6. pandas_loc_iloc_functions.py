import pandas as pd

df = pd.read_csv(r'C:\Users\bhatt\Downloads\sample2.csv', index_col = ['Roll No.'])
print(df.head())
print("\n==========================================")

print(df.loc[1])
print("\n==========================================")

print(df.loc[5])
print("\n==========================================")

print(df.loc[[5,6,7,8]])
print("\n==========================================")

print(df.loc[5, 'Physics'])
print("\n==========================================")

print(df.loc[5, 'DOB'])
print("\n==========================================")

print(df.loc[5:15, 'Chemistry'])
print("\n==========================================")

print(df.loc[df['Physics']<50])
print("\n==========================================")

print(df.loc[df['Physics']>80])
print("\n==========================================")

print(df.loc[df['Physics']>80, ['Maths']])
print("\n==========================================")



#     iloc()


print(df.iloc[0])
print("\n==========================================")

print(df.iloc[[0]])
print("\n==========================================")

print(df.iloc[:, 0])
print("\n==========================================")

print(df.iloc[:, 1])
print("\n==========================================")

print(df.iloc[0:5, 1])
print("\n==========================================")

print(df.iloc[0:5, 1:4])
print("\n==========================================")

