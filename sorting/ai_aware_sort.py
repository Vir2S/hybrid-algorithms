def ai_aware_sort(arr):
    if not arr:
        return arr

    # Detect types
    is_all_ints = all(isinstance(x, int) for x in arr)
    is_all_floats = all(isinstance(x, (int, float)) for x in arr)
    is_all_strings = all(isinstance(x, str) for x in arr)
    size = len(arr)

    try:
        if is_all_ints:
            value_range = max(arr) - min(arr)

            if value_range <= 1000:
                return counting_sort(arr)

            elif size <= 10000:
                quick_sort_inplace(arr, 0, size - 1)
                return arr

            else:
                return merge_sort(arr)

        if is_all_floats and all(0 <= x <= 1 for x in arr):
            return bucket_insertion_sort(arr, bucket_count=10)

        if is_all_strings:
            return merge_sort(arr)

        # Fallback: try sorting, if it fails, return unsorted
        return sorted(arr)

    except TypeError:
        print("❌ Cannot sort mixed types in fallback. Returning original array.")
        return arr


# ---------- Counting Sort ----------
def counting_sort(arr):
    min_val, max_val = min(arr), max(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


# ---------- Insertion Sort ----------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# ---------- Bucket + Insertion ----------
def bucket_insertion_sort(arr, bucket_count=10):
    min_val, max_val = min(arr), max(arr)
    range_size = (max_val - min_val) / bucket_count + 1e-9
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / range_size)
        buckets[index].append(num)

    sorted_arr = []

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


# ---------- QuickSort ----------
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------- MergeSort ----------
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


# ---------- Demo ----------
if __name__ == "__main__":
    from random import randint, uniform, choice

    ints_small_range = [randint(1, 100) for _ in range(20)]
    ints_large_range = [randint(1, 1000000) for _ in range(20)]
    floats_0_1 = [round(uniform(0, 1), 3) for _ in range(20)]
    strings = [choice(["apple", "orange", "banana", "kiwi", "pear"]) for _ in range(20)]
    mixed = [3, "banana", 0.5, 1000]

    print("Small-range ints:", ai_aware_sort(ints_small_range))
    print("Large-range ints:", ai_aware_sort(ints_large_range))
    print("Floats [0,1]:", ai_aware_sort(floats_0_1))
    print("Strings:", ai_aware_sort(strings))
    print("Fallback (mixed):", ai_aware_sort(mixed))
