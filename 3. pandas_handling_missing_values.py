import pandas as pd

df = pd.read_csv(r'C:\Users\bhatt\Downloads\sample.csv')
print(df.head())

print(df.isnull())
print("\n")

print(df.isnull().sum())
print("\n")

print(df.isnull().sum().sum())
print("\n")

  
'''       Dropping Rows with NaN Values       '''
      
print(df.shape)
print("\n")

df2 = df.dropna()   # default axis for dropna() is 0.
# dropna() drops all the rows consisting null values.

print(df2.shape)
print("\n")

'''       Dropping Columns with NaN Values       '''

df3 = df.dropna(axis = 1)  # axis = 1 for columns

print(df3.shape)
print("\n")

print(df.dropna(how = 'any'))  # if any row value is null, then remove that row.
print("\n")

print(df.dropna(how = 'all'))  # if all row values are null, then remove that row.
print("\n")

df.dropna(inplace = True)

print(df.shape)
print("\n")