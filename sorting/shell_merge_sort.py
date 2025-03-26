def shell_merge_sort(arr):
    # First, do a ShellSort pass to pre-sort the array
    shell_sort(arr)

    # Then finish with stable MergeSort for final ordering
    return merge_sort(arr)


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Standard ShellSort with gap reduction
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    # Standard merge operation
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Example usage:
if __name__ == "__main__":
    arr = [99, 45, 3, 22, 18, 5, 73, 61, 38, 11, 8, 92, 14, 29, 41, 2, 77, 30, 25]
    sorted_arr = shell_merge_sort(arr)
    print("Sorted array:", sorted_arr)
