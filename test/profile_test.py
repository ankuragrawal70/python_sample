import cProfile
from memory_profiler import profile
import dis
from itertools import groupby
#
# @profile(precision=10)
# def test_cpu():
#     l = []
#     for e in range(100):
#         l.append(e)
#     print(l)


# @profile(precision=10)

def test_v():
    x = []
    for i  in range(1000000):
        x.append(i)
    # print(x)


def test_x():
    x = [i for i in range(1000000)]

print(test_v.func_name)
print(dis.dis(test_v))

print(test_x.func_name)
print(dis.dis(test_x))

print()
# test_cpu()

# cProfile.run(test_cpu())