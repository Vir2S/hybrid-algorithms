def radix_merge_sort(arr):
    if not arr:
        return arr

    if not all(isinstance(x, int) for x in arr):
        raise TypeError("radixmerge_sort supports only integers.")

    negatives = [-x for x in arr if x < 0]
    zeros = [x for x in arr if x == 0]
    positives = [x for x in arr if x > 0]

    sorted_neg = radix_sort(negatives)
    sorted_pos = radix_sort(positives)

    # Combine: reverse negatives (since we used abs), then zeros, then positives
    return [-x for x in reversed(sorted_neg)] + zeros + sorted_pos


# ---------- Radix Sort (non-negative only) ----------
def radix_sort(arr):
    if not arr:
        return arr

    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement <= max_digit:
        buckets = [[] for _ in range(RADIX)]

        for num in arr:
            digit = (num // placement) % RADIX
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]
        placement *= RADIX

    return arr


# ---------- Demo ----------
if __name__ == "__main__":
    arr = [170, -45, 75, -90, 802, 24, 2, 66, -3, 0, -1000]
    print("Original:", arr)
    sorted_arr = radix_merge_sort(arr)
    print("Sorted:", sorted_arr)
