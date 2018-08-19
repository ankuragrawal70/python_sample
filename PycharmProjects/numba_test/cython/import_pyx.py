# import pyximport; pyximport.install()
from time import time
import test

if __name__ == '__main__':
    s = time()
    print (time())
    test.test_py(1000)
    e = time()
    print e - s