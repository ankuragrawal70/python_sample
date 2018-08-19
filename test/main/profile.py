import cProfile, pstats

from ds_algorithms.cythonize import integrate
cProfile.runctx("integrate.integrate_fun(10, 16666611, 1000000000)", globals(), locals(), "Profile.prof")
s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()


