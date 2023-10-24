import __init__
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=12345)
data = rng.standard_normal((2, 3))

# replicate loop instruments
points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)

print(xs**2 + ys**2)
z = xs**2 + ys**2
# plt.imshow(X=z, cmap="gray", extent=[-5, 5, -5, 5])
# plt.colorbar()
# plt.show()

# * Conditional logic
xs = np.array([1, 2, 3, 4, 5])
ys = 0 - xs

conds = np.array([True, False, True, False, True])

print(np.array([x if c else y for x, y, c in zip(xs, ys, conds)]))
print(np.where(conds, xs, ys))

# both scalar and arrays can be used
print(np.where(conds, 100, [1, 2, 3, 4, 5]))
print(np.where(conds, 100, ys))

# * methods of boolean arrays

arr = rng.standard_normal(100)

# use .sum() to count for the element satisfying the situation
print((arr > 0).sum())
print((arr < 0).sum())

# any() is True iff one element in the list satisfied the situation
print((arr > 0).any())

# all() is True iff every elemrnt in the list satisfied the situation
print((arr > 0).all())

# argmax to return the index first element satisfing the situaion

# sort() to sort the list
arr.sort()
print(arr)

# unique() to remove same element
ints = np.array([1, 1, 1, 1, 3, 3, 3, 3, 4, 5, 6, 7, 7, 7, 6, 55])


print(np.unique(ints))
