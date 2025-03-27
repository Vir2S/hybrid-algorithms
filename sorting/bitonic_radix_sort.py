def bitoradix_sort(arr):
    if not arr:
        return arr

    is_all_ints = all(isinstance(x, int) and x >= 0 for x in arr)

    # Case 1: Fast path — Radix + Bitonic for non-negative ints
    if is_all_ints:
        sorted_arr = radix_sort(arr)
        return bitonic_merge(sorted_arr, up=True)

    # Case 2: Fallback — use Python’s stable sort + Bitonic merge
    try:
        sorted_arr = sorted(arr)
        return bitonic_merge(sorted_arr, up=True)

    except TypeError:
        print("❌ Cannot sort array with incompatible mixed types. Returning original array.")
        return arr


# ---------- Radix Sort (for non-negative ints) ----------
def radix_sort(arr):
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


# ---------- Bitonic Merge ----------
def bitonic_merge(arr, up=True):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n // 2):
        if (arr[i] > arr[i + n // 2]) == up:
            arr[i], arr[i + n // 2] = arr[i + n // 2], arr[i]

    first_half = bitonic_merge(arr[:n // 2], up)
    second_half = bitonic_merge(arr[n // 2:], up)
    return first_half + second_half


# ---------- Demo ----------
if __name__ == "__main__":
    arr_int = [329, 457, 657, 839, 436, 720, 355, 66]
    arr_float = [3.14, 1.618, 2.718, 0.577, 4.669]
    arr_str = ["banana", "apple", "kiwi", "pear", "orange"]
    arr_mixed = [42, "banana", 3.14]

    print("Sorted ints:", bitoradix_sort(arr_int))
    print("Sorted floats:", bitoradix_sort(arr_float))
    print("Sorted strings:", bitoradix_sort(arr_str))
    print("Mixed types:", bitoradix_sort(arr_mixed))  # fallback with warning
