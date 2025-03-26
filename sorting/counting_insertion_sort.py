def counting_insertion_sort(arr, max_range=1000):
    # Check if array is suitable for CountingSort
    if arr and (max(arr) - min(arr)) <= max_range:
        return counting_sort(arr)
    insertion_sort(arr)
    return arr


def counting_sort(arr):
    min_val, max_val = min(arr), max(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize the counting array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count each element
    for num in arr:
        count[num - min_val] += 1

    # Accumulate counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the sorted array
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
if __name__ == "__main__":
    arr_small_range = [15, 3, 7, 8, 3, 12, 5, 9, 7, 3]
    arr_large_range = [1023, 5000, 7000, 3, 1200, 3000, 9000, 7, 4500]

    sorted_small = counting_insertion_sort(arr_small_range)
    sorted_large = counting_insertion_sort(arr_large_range)

    print("Sorted small-range array (CountingSort):", sorted_small)
    print("Sorted large-range array (InsertionSort):", sorted_large)
