import numpy as np
import pandas as pd


def test_method(arr):
    arr[0, 0] = 22

arr = np.array([[14, 16, 18, 20],[12, 45, 55, 25]], dtype='int')
print arr[0, 0]

test_method(arr)
print arr
# print arr
# print "\n\n"
# print arr[0:2, 0:2]
# print "\n\n"
# print arr[::-1, ::-1]

# print type(np.datetime64('2005-02-25'))
# print pd.Series(pd.date_range('2012-1-1', periods=100, freq='D'))
