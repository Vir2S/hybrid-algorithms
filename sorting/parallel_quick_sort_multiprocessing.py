import multiprocessing


def parallel_quick_sort_mp(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with multiprocessing.Pool(2) as pool:
        sorted_left, sorted_right = pool.map(parallel_quick_sort_mp, [left, right])

    return sorted_left + middle + sorted_right


#  Usage example
if __name__ == '__main__':
    arr = [42, 15, 3, 9, 27, 34, 1, 18, 7, 88, 65, 99, 14, 20]
    sorted_arr = parallel_quick_sort_mp(arr)
    print(sorted_arr)
