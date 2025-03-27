def shell_bucket_sort(arr, bucket_count=10):
    if not arr:
        return arr

    # Detect number range
    min_val, max_val = min(arr), max(arr)
    range_size = (max_val - min_val) / bucket_count + 1e-9  # to avoid division by zero

    # Create buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / range_size)
        buckets[index].append(num)

    # Sort each bucket using Shell Sort
    sorted_arr = []

    for bucket in buckets:
        shell_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


# ---------- Shell Sort ----------
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


# ---------- Demo ----------
if __name__ == "__main__":
    from random import uniform
    arr = [round(uniform(0, 100), 2) for _ in range(25)]
    print("Original:", arr)
    sorted_arr = shell_bucket_sort(arr)
    print("Sorted:", sorted_arr)
