import numpy as np

print((np.exp(0.03 / 12) - np.exp(-0.25 * np.sqrt(1 / 12))) /
      (np.exp(0.25 * np.sqrt(1 / 12)) - np.exp(-0.25 * np.sqrt(1 / 12))))
