def shell_quick_sort(arr):
    # First pass with Shell Sort to reduce disorder
    shell_sort(arr)

    # Then finish sorting with Quick Sort
    quick_sort_inplace(arr, 0, len(arr) - 1)
    return arr


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


# ---------- Example usage ----------
if __name__ == "__main__":
    arr = [45, 3, 22, 18, 5, 73, 61, 38, 11, 8, 92, 14, 29, 41, 2, 77, 30, 25]
    sorted_arr = shell_quick_sort(arr)
    print("Sorted array:", sorted_arr)
