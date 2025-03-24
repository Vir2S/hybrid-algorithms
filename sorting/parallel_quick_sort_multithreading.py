import concurrent.futures


def parallel_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # If big array sorting parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        left_future = executor.submit(parallel_quick_sort, left)
        right_future = executor.submit(parallel_quick_sort, right)
        sorted_left = left_future.result()
        sorted_right = right_future.result()

    return sorted_left + middle + sorted_right


#  Usage example
arr = [42, 15, 3, 9, 27, 34, 1, 18, 7, 88, 65, 99, 14, 20]
sorted_arr = parallel_quick_sort(arr)
print(sorted_arr)
