import time
from time import time
# import random
# import numpy as np

# import pyximport
# pyximport.install()
#
# from ds_algorithms import selection_sort as ds_sel
from ds_algorithms.cythonize import integrate

try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner









# from ds_algorithms.cythonize import integrate
# import cProfile, line_profiler
# n = 100000import cProfile, pstats
# t = []
# t = np.zeros(n,1)


# line_profiler.LineProfiler()

@do_profile
def time_func(func, *arr):
    # start = time()
    func(*arr)
    # print(str(time()-start) + " seconds")

#
# for i in range(0, n):
#     t.append(random.randint(1, n))
#
#
# print(len(t))
# # arr = np.array(t, dtype=np.int32)
#time_func(selection_sort.selection_sort, arr)
# time_func(selection_sort.s_sort, arr)
# time_func(ds_sel.s_sort, arr)
# time_func(ds_sel.selection_sort, arr)




# cProfile.run("integrate.integrate_fun(10, 16666611, 1000000000)")
# s = pstats.Stats("Profile.prof")
# s.strip_dirs().sort_stats("time").print_stats()


time_func(integrate.integrate_fun, 10, 16666611, 1000000000)
# cProfile.run("time_func(integrate.integrate_fun, 10, 16666611, 1000000000)")
# time_func(integrate.integrate_fun, 10, 16666611, 1000000000)
# cProfile.run("time_func(integrate.integrate_fun, 10, 16666611, 1000000000)")

# for i in range(0, 100):
#     time_func(integrate.integrate_fun, 10, 16666611, 1000000000)
# cProfile.run("integrate.integrate_fun(10, 16666611, 1000000000)")
# start = time.time()
# print(integrate.integrate_fun(10, 16666611, 1000000000))
#
# @do_profile
# integrate.integrate_fun(10, 16666610, 1000000000)
# integrate.integrate_fun(10, 16666611, 1000000000)
# integrate.integrate_fun(10, 16666611, 1000000000)
# print(time.time() - start)