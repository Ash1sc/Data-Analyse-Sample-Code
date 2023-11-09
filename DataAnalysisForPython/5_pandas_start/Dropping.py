import pandas as pd
import numpy as np

# can dropping by reindexing with a new index or columns containing the entries you want to remain in the object

# drop method return a new object with the indicated value or values deleted from an axis

# * Series
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
new_obj = obj.drop("c")
obj.drop(["d", "c"])

# * DataFrame
# data can be deleted from either axis, specific the axis by using index or columns
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])

print(data.drop(index=["Colorado", "Ohio"]))
print(data.drop(["Colorado", "Ohio"]))
print(data.drop(columns=["two"]))
print(data.drop(["two"], axis=1))
