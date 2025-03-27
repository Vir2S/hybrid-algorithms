def radix_quick_sort(arr, max_radix_range=1000):
    # Check if the array can be efficiently sorted with RadixSort
    if arr and max(arr) - min(arr) <= max_radix_range:
        return radix_sort(arr)

    quick_sort_inplace(arr, 0, len(arr) - 1)
    return arr


def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement <= max_digit:
        # Create buckets for digits 0-9
        buckets = [[] for _ in range(RADIX)]

        for num in arr:
            digit = (num // placement) % RADIX
            buckets[digit].append(num)

        # Flatten the buckets into the array
        arr = [num for bucket in buckets for num in bucket]

        placement *= RADIX

    return arr


def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # pivot chosen as the last element
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage:
if __name__ == "__main__":
    arr_small_range = [23, 5, 7, 12, 3, 9, 17, 45, 8, 15]
    arr_large_range = [1023, 5, 15000, 7, 800, 12, 3, 9999, 17, 45000]

    sorted_small = radix_quick_sort(arr_small_range)
    sorted_large = radix_quick_sort(arr_large_range)

    print("Sorted small-range array (RadixSort):", sorted_small)
    print("Sorted large-range array (QuickSort):", sorted_large)
