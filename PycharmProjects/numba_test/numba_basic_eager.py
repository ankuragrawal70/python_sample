from numba import jit, int32, void
from time import time


def f(x, y):
    # A somewhat trivial example
    s = time()
    # print ("time without numba start", s)
    e = time()
    # print ("time without numba end", e)
    print ("execution time without numba", e - s)
    return x + y


@jit(void(int32, int32))
def f_numba(x, y):
    # return x + y
    print (x+y)
print (f(12, 32))
print f_numba(12, 32)