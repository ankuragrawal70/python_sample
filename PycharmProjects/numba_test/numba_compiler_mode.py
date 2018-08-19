from numba import jit, int32
import numpy as np
import gc
from time import time
# print ("Garbage collection thresholds:", gc.get_threshold())
print (gc.collect())
gc.enable()


@jit
def covariance_m():
    print (time())
    x = np.arange(360000).reshape(600, 600)
    n = x * 100
    print(np.cov(x))
    print (time())
    print (n)
    # print (np.tril())

covariance_m()

print (gc.collect())
print (gc.enable())