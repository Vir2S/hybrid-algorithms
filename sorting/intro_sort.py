import math
import heapq


def intro_sort(arr):
    max_depth = 2 * math.floor(math.log2(len(arr)))
    _intro_sort_helper(arr, 0, len(arr) - 1, max_depth)


def _intro_sort_helper(arr, start, end, max_depth, threshold=16):
    size = end - start + 1

    # Use InsertionSort for small subarrays
    if size <= threshold:
        insertion_sort(arr, start, end)
        return

    # Use HeapSort if depth limit is reached
    if max_depth == 0:
        heap_sort_subarray(arr, start, end)
        return

    # Standard QuickSort partition
    pivot_index = partition(arr, start, end)
    _intro_sort_helper(arr, start, pivot_index - 1, max_depth - 1)
    _intro_sort_helper(arr, pivot_index + 1, end, max_depth - 1)


def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1

        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heap_sort_subarray(arr, start, end):
    sub = arr[start:end+1]
    heapq.heapify(sub)

    for i in range(start, end + 1):
        arr[i] = heapq.heappop(sub)


def partition(arr, low, high):
    pivot = arr[high]  # choose last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage:
if __name__ == "__main__":
    arr = [99, 45, 3, 22, 18, 5, 73, 61, 38, 11, 8, 92, 14, 29, 41, 2, 77, 30, 25]
    intro_sort(arr)
    print("Sorted array:", arr)
