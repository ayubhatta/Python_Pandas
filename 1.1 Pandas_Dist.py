import pandas as pd

# PANDAS SERIES WITH PYTHON DICTIONARIES

dict_series = pd.Series({'p':1, 'q':2, 'r':3, 's':4, 't':5})    # dictionary type
print(dict_series)
print("\n")

print(dict_series[4])
print(dict_series[0:4])
print("\n")

print(max(dict_series))
print("\n")

dict_series = pd.Series({'p':[1,5,6], 'q':[2,6,7], 'r':[3,9,0], 's':[4,4,5], 't':[5,1,2]})
print(dict_series)
