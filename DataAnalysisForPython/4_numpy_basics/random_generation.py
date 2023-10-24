import __init__

import numpy as np

# np.random is more powerful than the built-in module random,
# can generate an multi-dimension array of random numbers

# a explicit random generator can be used
rng = np.random.default_rng(seed=12345)
data = rng.standard_normal((2, 3))
