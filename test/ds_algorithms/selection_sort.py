import numpy as np
def selection_sort(arr):
    for i, e in enumerate(arr):
        min = arr[i]
        flag = 0
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                flag = 1
        if flag > 0:
            flag = 0
            arr[i], arr[flag] = arr[flag], arr[i]



def s_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    #return x