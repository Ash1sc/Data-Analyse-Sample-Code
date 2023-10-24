import __init__
import numpy as np
import matplotlib.pyplot as plt

nsteps = 1000

# * single walk
rng = np.random.default_rng(seed=12345)
steps = np.where(rng.integers(0, 2, size=nsteps) == 1, 1, -1)
walk = np.cumsum(steps)

# plt.plot(walk)
# plt.show()

print((np.abs(walk) >= 10).argmax())

# * multiple walk
nwalk = 5000
steps = np.where(rng.integers(0, 2, size=(nwalk, nsteps)) == 1, 1, -1)
walk = np.cumsum(steps, axis=1)

print((np.abs(walk) >= 30).any(axis=1).sum())

print((np.abs(walk[(np.abs(walk) >= 30).any(axis=1)]) >= 30).argmax(axis=1))
