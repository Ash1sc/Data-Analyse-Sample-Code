import pandas as pd
import numpy as np

from pandas import Series, DataFrame


# * Series in pandas, like a fixed-length,ordered dict

# construct from array-like data
obj = pd.Series([4, 7, -5, 3])
obj = pd.Series((1, 2, 3))
obj = pd.Series(np.array([4, 7, -5, 3]))
print(obj)

# get data and index seperatly

print(obj.array)
print(obj.index)

# construct with index
obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])

print(obj2["d"])
print(obj2[["d", "c", "b"]])

# preserve index-value link while filering the list or applying math operations

print(obj2[obj2 > 0])
print(obj2 * 2)

# construct with dict
sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
obj3 = pd.Series(sdata)
print(obj3)

# series convert to dict
print("Convert obj3 to dict")
print(obj3.to_dict())

# pass a list of index to reordering the keys in the dict
obj4 = pd.Series(sdata, index=["California", "Ohio", "Oregon", "Texas"])

# name the object and index
obj4.name = "population"
obj4.index.name = "states"
print(obj4)
