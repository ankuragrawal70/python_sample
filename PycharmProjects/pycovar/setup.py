from distutils.core import setup
from Cython.Build import cythonize
# from setuptools import Extension
import numpy as np
# from setuptools import find_packages


SRC_DIR = 'buildercovar'
packages = [SRC_DIR]
# st = cythonize(SRC_DIR + "/test.pyx")
# print st[0].__dict__
# ext_1 = Extension(cythonize(SRC_DIR + "/test.pyx"))

f = SRC_DIR + "/*.pyx"
y = "db" + "/*.pyx"
# print find_packages()
# for i in  cythonize([f, y]):
#     print i.__dict__
setup(ext_modules=cythonize([f, y], annotate=True))