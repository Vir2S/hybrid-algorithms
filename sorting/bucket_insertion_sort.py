def bucket_insertion_sort(arr, bucket_count=10):
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    range_size = (max_val - min_val) / bucket_count + 1e-9  # avoid division by zero

    # Initialize buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / range_size)
        buckets[index].append(num)

    # Sort each bucket using Insertion Sort and concatenate
    sorted_arr = []

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


# ---------- Insertion Sort ----------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# ---------- Example usage ----------
if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    sorted_arr = bucket_insertion_sort(arr, bucket_count=5)
    print("Sorted array:", sorted_arr)
