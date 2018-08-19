import numpy as np
x = np.arange(36000000).reshape(6000, 6000)

print(np.cov(x))