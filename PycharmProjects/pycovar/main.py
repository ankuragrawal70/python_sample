from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from buildercovar import test
from buildercovar import primes
from db import sum

import numpy as np
arr = np.array([[1, 4, 6],[2, 4, 5]], dtype=np.int32)
print (arr)
test.np_array(arr)
print (arr)


a=(sum.sum(100000000000000000000000, 200000000000000000))
print (a)