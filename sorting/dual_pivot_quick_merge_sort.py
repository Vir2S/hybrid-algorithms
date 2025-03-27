def dpq_merge_sort(arr):
    if not arr:
        return arr

    # If array is small or "messy" — go dual-pivot quicksort
    if len(arr) <= 32 or is_messy(arr):
        dual_pivot_quicksort(arr, 0, len(arr) - 1)
        return arr

    # Otherwise use MergeSort
    return merge_sort(arr)


# ---------- Entropy Checker ----------
def is_messy(arr):
    count = sum(1 for i in range(1, len(arr)) if arr[i] < arr[i - 1])
    return count > len(arr) // 3  # >33% disorder is messy


# ---------- Dual Pivot QuickSort ----------
def dual_pivot_quicksort(arr, low, high):
    if low < high:
        lp, rp = partition_dual_pivot(arr, low, high)
        dual_pivot_quicksort(arr, low, lp - 1)
        dual_pivot_quicksort(arr, lp + 1, rp - 1)
        dual_pivot_quicksort(arr, rp + 1, high)


def partition_dual_pivot(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    pivot1 = arr[low]
    pivot2 = arr[high]

    i = low + 1
    lt = low + 1
    gt = high - 1

    while i <= gt:

        if arr[i] < pivot1:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1

        elif arr[i] > pivot2:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
            i -= 1

        i += 1

    lt -= 1
    gt += 1
    arr[low], arr[lt] = arr[lt], arr[low]
    arr[high], arr[gt] = arr[gt], arr[high]

    return lt, gt


# ---------- MergeSort ----------
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


# ---------- Demo ----------
if __name__ == "__main__":
    messy = [33, 12, 1, 99, 2, 77, 14, 4, 50, 3, 21, 8, 66]
    sorted_like = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Messy (DPQ):", dpq_merge_sort(messy.copy()))
    print("Sorted-like (Merge):", dpq_merge_sort(sorted_like.copy()))
