def fun(x):
    return x *x - x


def integrate_py(first, second, times):
    #s = time.time()
    result = 0
    dx = (second - first) / times
    for i in range(times):
        result += fun(first + i * dx)
    ret = result * dx
    #print time.time() - s
    return ret