def merge_insertion_sort(arr, threshold=32):
    # If array is small enough, use InsertionSort
    if len(arr) <= threshold:
        insertion_sort(arr)
        return arr

    # Split array into two halves
    mid = len(arr) // 2
    left = merge_insertion_sort(arr[:mid], threshold)
    right = merge_insertion_sort(arr[mid:], threshold)

    # Merge sorted halves
    return merge(left, right)


def insertion_sort(arr):
    # Standard insertion sort implementation
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(left, right):
    result = []
    i = j = 0
    # Merge two sorted lists into a single sorted list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements, if any
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage:
if __name__ == "__main__":
    arr = [42, 33, 17, 8, 99, 23, 5, 7, 88, 1, 56, 20, 15, 2, 78]
    sorted_arr = merge_insertion_sort(arr)
    print("Sorted array:", sorted_arr)
