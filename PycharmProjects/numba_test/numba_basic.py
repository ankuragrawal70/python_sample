from numba import jit, int32, float32
from numpy import arange
from time import time
import gc

# print ("Garbage collection thresholds:", gc.get_threshold())
print (gc.collect())


@jit
def sum2d(arr):
    print (time())
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    print (time())
    return result

a = arange(9000000).reshape(3000,3000)
# print(sum2d(a))


# @jit(float32, float32)
def simple_sum():
    s = time()
    print ("start time is", s)
    # M, N = arr.shape
    result = 0.0
    # for i in range(M):
    #     for j in range(N):
    #         result += arr[i,j]
    # s = 0
    for i in range(0, 1000000000):
        result += i
    e = time()
    print ("end time is", e)
    diff = e - s
    print ("time taken", diff)
    return result

print (simple_sum())
print (simple_sum())
# @jit(int32(int32, int32))
# def f(x, y):
#     # A somewhat trivial example
#     return x + y
#
# print (f(10, 20))

print (gc.collect())
print ("Garbage collection thresholds:", gc.get_threshold())
gc.enable()
print gc.collect()