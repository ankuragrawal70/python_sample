import random
import time


def heapify_down(i, arr):
    if i >= len(arr):
        return

    l = 2*i + 1
    r = l + 1
    index = i
    max = arr[i]
    if l<len(arr) and arr[l] > max:
        max, index = arr[l], l
    if r < len(arr) and arr[r] > max:
        max, index = arr[r], r
    if index != i:
        arr[i], arr[index] = arr[index], arr[i]
        heapify_down(index, arr)
    else:
        return


def build_max_heap(arr):
    for i in xrange(len(arr)/2, -1, -1):
        heapify_down(i, arr)


def heap_sort(arr):
    build_max_heap(arr)
    length = len(arr)
    print("max heap", arr)
    s = length -1
    for i in xrange(s, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_down(0, arr[0:i])


if __name__ == "__main__":
    t = []
    n = 10
    for e in range(0, n):
        t.append(random.randint(1, n))
    for i in range(0, len(t)):
        t[i] = random.randint(1, n)
    print(t)
    start = time.time()
    print("starting time", start)
    heap_sort(t)
    print(t)
    end = time.time()
    print(end)
    print(end - start)




