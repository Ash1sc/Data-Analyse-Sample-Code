# Dataframe have both a row and colume index
# like a dictionary of different series with same index
import pandas as pd
import numpy as np


# * construtcion
"""_summary_
    construct from a dictionary, most common. 
    the order of colume in the dataframe depend on the inserted order in the dictionary.
"""
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print("-------------constructing dataframe from dictionary----------")
print(frame)

# * constructing dataframe from nested dictionary
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}, "Nevada": {2001: 2.4, 2002: 2.9}}
frame3 = pd.DataFrame(populations)
print("----------constructing dataframe from nested dictionary")
print(frame3)

# * transform the dataframe to .T

print(frame3.T)

# head to return the first five rows
# tail to return the last five rows

print(frame.head())
print(frame.tail(5))

# arranged the order of the colume
frame2 = pd.DataFrame(data, columns=["year", "state", "pop"])
print("arrange the order of column")
print(frame2)

# non-exist column index in the column attribute will be filled in with NaN

frame2 = pd.DataFrame(data, columns=["year", "state1", "pop1"])
print(frame2)

# arranged the order of the row using index
print("-----------arrange the order of row-------------")
print(pd.DataFrame(populations, index=[2001, 2002, 2003]))

# * get a column in the dataframe
# the index of the column will be used as the column's name attribute
# 1. works for any column name
print(frame["year"])
# 2. for column name as avslid Python variable name and not conflict with any method
print(frame.year)

# * get a row
print(frame.loc[1])
print(frame.iloc[1])

# * column can be assigned as a Series
frame2["new column"] = 3
print(frame2)

# sign a column with Series ,data will find the row in the dataframe according to their index in the series
frame2["pop1"] = pd.Series(data=[0, 1, 2, 3, 4, 5], index=[5, 4, 3, 2, 1, 0])
print(frame2)

# * delete the column in the dataframe
del frame2["new column"]
print(frame2)

# * convert dataframe to numpy 2D-array
print(frame3.to_numpy())
