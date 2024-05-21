import sorting
import timeit


def test(arr):
    res = sorting.hybrid_sort(arr.copy())
    hybrid_time = timeit.timeit(lambda: sorting.hybrid_sort(arr.copy()), setup="pass", number=20)
    heap_time = timeit.timeit(lambda: sorting.heap_sort(arr.copy()), setup="pass", number=20)
    quick_time = timeit.timeit(lambda: sorting.quick_sort(arr.copy()), setup="pass", number=20)
    return hybrid_time, heap_time, quick_time, res
