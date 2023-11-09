import numpy as np
import pandas as pd


# * Series
# same as indexing numpy.array but can also index with index of series
obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
print(obj["b"])
print(obj[1])
print(obj[2:4])
print(obj[["b", "a", "d"]])
print(obj[[1, 3]])
print(obj[obj < 2])

# prefer way is to select with loc operator
# if series index have integers, python will treat the number as the index i nthe series
print(obj.loc[["a", "b", "c"]])
# loc indexes exclusively with labels
# iloc indexed exlusively with integers
obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])
obj2 = pd.Series([1, 2, 3], index=["a", "b", "c"])

print(obj1.loc[[0, 1, 2]])
print(obj1.iloc[[0, 1, 2]])

# can slice with label
# but include the stopped index
# loc[0:2] contains 0,1,2

print(obj1.loc[0:2])
print(obj1.iloc[0:2])
print(obj2.loc["a":"c"])

# * DataFrame
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=[
                    "Ohio", "Colorado", "Utah", "New York"], columns=["one", "two", "three", "four"])

# select with a boolean list
print(data[data["three"] > 5])

# can only filter columns
print(data[["one", "two"]])

# using loc([index], [columns]) and iloc()

# boolean selection can only be used with .loc

print(data.loc[data.three > 2])

# integer piffull
# if have integer index, python will use index filter instead of positon filter
# 如果不用integer作为下标，则无混淆，可以使用
# prefer to use .loc[] for index filter, .iloc[] for positon filter

# chained indexing pitfalls
# call a chained function list like:__get_item__.__set_item__, where weather getitem return a copy or orignal sub object is unpredictable 
data.loc[data.two == 5]["three"] = 6
