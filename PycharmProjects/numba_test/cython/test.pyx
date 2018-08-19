def test_py(limit):
    cdef int result = 0
    cdef int a = 0
    cdef int b = 0
    cdef int c = 0
    cdef int p[100]
    result = 0
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if c * c > a * a + b * b:
                    break

                if c * c == (a * a + b * b):
                    result += 1
    p[1] = 232
    #print p
    #for i in range(0, len(p)):
    #    print p[i]
    return result


def test_np(arr):
    arr[0, 0] = 20
