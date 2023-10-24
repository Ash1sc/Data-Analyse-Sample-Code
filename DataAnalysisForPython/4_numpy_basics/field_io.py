import __init__
import numpy as np

arr = np.arange(10)

np.save("tmp", arr)
print(np.load("tmp.npy"))
