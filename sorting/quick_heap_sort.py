import heapq
import math


def quick_heap_sort(arr):
    max_depth = 2 * math.floor(math.log2(len(arr)))
    _quick_heap_sort_helper(arr, 0, len(arr) - 1, max_depth)


def _quick_heap_sort_helper(arr, low, high, depth_limit):
    if low < high:
        # If recursion depth limit is reached, use HeapSort
        if depth_limit == 0:
            heap_sort_subarray(arr, low, high)
            return

        pivot_index = partition(arr, low, high)
        _quick_heap_sort_helper(arr, low, pivot_index - 1, depth_limit - 1)
        _quick_heap_sort_helper(arr, pivot_index + 1, high, depth_limit - 1)


def partition(arr, low, high):
    pivot = arr[high]  # Pivot chosen as the last element
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort_subarray(arr, low, high):
    # Perform HeapSort on a subarray
    subarray = arr[low:high + 1]
    heapq.heapify(subarray)
    for i in range(low, high + 1):
        arr[i] = heapq.heappop(subarray)


# Example usage:
if __name__ == "__main__":
    arr = [99, 45, 3, 22, 18, 5, 73, 61, 38, 11, 8, 92, 14, 29, 41, 2, 77, 30, 25]
    quick_heap_sort(arr)
    print("Sorted array:", arr)
