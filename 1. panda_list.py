'''Pandas is a fast, powerful, flexible and easy to use open source data 
analysis and manipulation tool, built on top of the Python Programming Language'''

import pandas as pd

# PANDAS SERIES WITH PYTHON LISTS

lst = [1,2,3,4,5]      # list
print(lst)
print("\n")

series = pd.Series(lst)
print(series)
print(type(series))
print("\n")

empty = pd.Series([])
print(empty)
print("\n")

a = pd.Series(['p','q','r','s','t'], index = [10,11,12,13,14])
print(a)
print("\n")

b = pd.Series(['p','q','r','s','t'], index = [10,11,12,13,14], name = 'alphabet')
print(b)
print("\n")

scalar_series = pd.Series(0.5)
print(scalar_series)
print("\n")

scalar_series = pd.Series(0.5, index = [1,2,3])
print(scalar_series)


