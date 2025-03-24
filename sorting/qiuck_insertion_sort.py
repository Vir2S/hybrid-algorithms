def quick_insertion_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    # InsertionSort, if pars is small
    if high - low <= 10:
        insertion_sort(arr, low, high)
        return

    if low < high:
        pivot = partition(arr, low, high)
        quick_insertion_sort(arr, low, pivot - 1)
        quick_insertion_sort(arr, pivot + 1, high)


def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


#  Usage example
arr = [34, 2, 78, 1, 56, 99, 23, 4, 15, 42, 66, 7]
quick_insertion_sort(arr)
print(arr)  # [1, 2, 4, 7, 15, 23, 34, 42, 56, 66, 78, 99]
