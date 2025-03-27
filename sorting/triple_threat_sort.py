def triple_threat_sort(arr):
    if not arr:
        return arr

    # Check if all elements are integers
    is_all_ints = all(isinstance(x, int) for x in arr)

    if is_all_ints:
        min_val, max_val = min(arr), max(arr)
        value_range = max_val - min_val

        # Case 1: Small integer range → Radix Sort
        if value_range <= 1000:
            return radix_sort(arr)

        # Case 2: Large integer range but array not too big → QuickSort
        elif len(arr) <= 10000:
            quick_sort_inplace(arr, 0, len(arr) - 1)
            return arr

    # Case 3: Everything else → MergeSort
    return merge_sort(arr)


# ---------- Radix Sort ----------
def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement <= max_digit:
        buckets = [[] for _ in range(RADIX)]

        for num in arr:
            digit = (num // placement) % RADIX
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]
        placement *= RADIX

    return arr


# ---------- Quick Sort ----------
def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------- Merge Sort ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- Example usage ----------
if __name__ == "__main__":
    arr_small_range = [5, 3, 17, 9, 11, 1, 4, 2, 6, 8, 7]
    arr_large_range = [15000, 923, 128000, 1, 34999, 77777, 5, 75000]
    arr_strings = ["pear", "apple", "banana", "orange", "kiwi", "grape"]

    print("Sorted small-range ints (Radix):", triple_threat_sort(arr_small_range))
    print("Sorted large-range ints (Quick):", triple_threat_sort(arr_large_range))
    print("Sorted strings (Merge):", triple_threat_sort(arr_strings))
