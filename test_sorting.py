import sorting
import timeit


def test(arr):
    res = sorting.hybrid_sort(arr)
    hybrid_time = timeit.timeit(lambda: sorting.hybrid_sort(arr), setup="pass", number=10)
    heap_time = timeit.timeit(lambda: sorting.heap_sort(arr), setup="pass", number=10)
    quick_time = timeit.timeit(lambda: sorting.quick_sort(arr), setup="pass", number=10)
    return hybrid_time, heap_time, quick_time, res
