import __init__
import util.setup
import datetime
import numpy as np

b = [1, 2, 3]
print(hasattr(b, "__iadd__"))

tmp = util.setup.c(3)   
print(tmp.get_attr())
print(hasattr(tmp, "get_attr"))
print(dir(tmp))
print(str(tmp))


# timedata class
dt1 = datetime.datetime(2023, 10, 17, 13, 30, 30)
dt2=datetime.datetime(2022, 10, 17, 13, 30, 30)

print(dt1.strftime("%Y/%m/%d %H:%M"))
print(dt2.strftime("%Y/%m/%d %H:%M"))

delta=dt1-dt2
print(type(delta))
print(type(dt1-delta))
print(type(dt1+delta))