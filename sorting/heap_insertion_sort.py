import heapq


def heap_insertion_sort(arr, threshold=16):
    if len(arr) <= threshold:
        insertion_sort(arr)
        return arr

    # Create heap
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
arr = [42, 33, 17, 8, 99, 23, 5, 7, 88, 1, 56, 20]
sorted_arr = heap_insertion_sort(arr)
print(sorted_arr)
