#from cython import boundscheck, wraparound
import numpy as np
#@boundscheck(False)
#@wraparound(False)

def selection_sort(int[:] arr):
    cdef int i
    cdef int e
    cdef int min, flag, j
    cdef int le = len(arr)
    for i in range(0, len(arr)):
        e = arr[i]
        min = arr[i]
        flag = 0
        j = i+1
        for j in range(j, le):
            if arr[j] < min:
                min = arr[j]
                flag = 1
        if flag > 0:
            flag = 0
            arr[i], arr[flag] = arr[flag], arr[i]




def s_sort(int[:] x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    #return x


