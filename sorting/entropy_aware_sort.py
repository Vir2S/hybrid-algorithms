def entro_sort(arr):
    if not arr:
        return arr

    disorder_ratio = measure_disorder(arr)

    if disorder_ratio <= 0.05:
        insertion_sort(arr)
        print("→ InsertionSort used")
        return arr

    elif disorder_ratio <= 0.3:
        print("→ MergeSort used")
        return merge_sort(arr)

    elif disorder_ratio <= 0.7:
        quick_sort_inplace(arr, 0, len(arr) - 1)
        print("→ QuickSort used")
        return arr

    else:
        heap_sort(arr)
        print("→ HeapSort used")
        return arr


# ---------- Disorder Meter ----------
def measure_disorder(arr):
    if len(arr) < 2:
        return 0

    disorder = sum(1 for i in range(1, len(arr)) if arr[i] < arr[i - 1])
    return disorder / (len(arr) - 1)


# ---------- Insertion Sort ----------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# ---------- Merge Sort ----------
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


# ---------- Quick Sort ----------
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


# ---------- Heap Sort ----------
def heap_sort(arr):
    import heapq
    temp = arr.copy()
    heapq.heapify(temp)
    arr[:] = [heapq.heappop(temp) for _ in range(len(temp))]


# ---------- Demo ----------
if __name__ == "__main__":
    almost_sorted = [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]
    half_mess = [1, 5, 3, 2, 4, 9, 8, 6, 10, 7]
    fully_messy = [99, 23, 11, 8, 7, 19, 3, 1, 0, -5]
    disaster = [i for i in range(1000, 0, -1)]

    print("\nSorting: almost_sorted")
    print("Result:", entro_sort(almost_sorted.copy()))
    print("\nSorting: half_mess")
    print("Result:", entro_sort(half_mess.copy()))
    print("\nSorting: fully_messy")
    print("Result:", entro_sort(fully_messy.copy()))
    print("\nSorting: disaster (worst-case)")
    print("Result:", entro_sort(disaster.copy()[:20]))
