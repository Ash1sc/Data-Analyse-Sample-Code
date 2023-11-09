import numpy as np
import pandas as pd


# * Series
# create a new object with the values rearranged to align with the new index
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
print("---------print obj-------------")
print(obj)

# use new list of index to reindex a series
obj2 = obj.reindex(["a", "b", "c", "d", "e"])

# method option to create NaN element in the desired way
obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
obj3 = obj3.reindex(np.arange(6), method="ffill")
print(obj3)

# *Dataframe
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=["a", "c", "d"], columns=["Ohio", "Texas", "California"])

# reindex the index or columns
frame2 = frame.reindex(index=["a", "b", "c", "d"])
frame2 = frame.reindex(["a", "b", "c", "d"], axis="index")
frame2 = frame.reindex(["a", "b", "c", "d"], axis=0)
print(frame2)
frame3 = frame = frame.reindex(columns=["Ohio", "Texas", "California"])
frame3 = frame.reindex(["Ohio", "Texas", "California"], axis="columns")
frame3 = frame.reindex(["Ohio", "Texas", "California"], axis=1)
print(frame3)
