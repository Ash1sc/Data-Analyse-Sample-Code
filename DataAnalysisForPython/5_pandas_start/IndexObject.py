# index object in responsible to hold the axis labels and other metadata
# Series has attribute, series's index has name
# dataframe doesn't have name, but have columuns and index, and both of them have name attribute
import pandas as pd
import numpy as np


obj = pd.Series(np.arange(3), index=["a", "b", "c"])

index = obj.index
print("----------print index of obj------------")
print(index)
# * index are immutable
# * being both array-like and fixed-size set-like
labels = pd.Index(np.arange(3))
labels2 = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print("----------print pbj2-------------")
print(obj2)
print(obj2.index is labels2)

print("a" in obj.index)
