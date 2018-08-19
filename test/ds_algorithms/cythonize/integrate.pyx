#import time


cdef double fun(double x):
    return x *x - x


def integrate_fun(double first, double second, long times):
    #s = time.time()
    cdef int i
    cdef double result, dx
    result = 0
    dx = (second - first) / times
    for i in range(times):
        result += fun(first + i * dx)
    ret = result * dx
    #print time.time() - s
    print ret
    return ret
