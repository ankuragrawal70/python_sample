from distutils.core import setup
from Cython.Build import cythonize
import os

SRC_DIR = 'test'
DS_DIR = os.path.join(SRC_DIR, "data_structure")

packages = [SRC_DIR]


f = "ds_algorithms/"+ "cythonize" + "/*.pyx"
# y = "db" + "/*.pyx"

print("f is ", f)
# setup(ext_modules=cythonize([f, y], annotate=True))
setup(ext_modules=cythonize([f,], annotate=True))