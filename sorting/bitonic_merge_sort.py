def bitonic_sort(arr, up=True):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    first_half = bitonic_sort(arr[:mid], True)
    second_half = bitonic_sort(arr[mid:], False)

    return bitonic_merge(first_half + second_half, up)


def bitonic_merge(arr, up):
    n = len(arr)

    if n <= 1:
        return arr

    # Compare and swap
    for i in range(n // 2):

        if (arr[i] > arr[i + n // 2]) == up:
            arr[i], arr[i + n // 2] = arr[i + n // 2], arr[i]

    # Recursively merge subarrays
    first_half = bitonic_merge(arr[:n // 2], up)
    second_half = bitonic_merge(arr[n // 2:], up)
    return first_half + second_half


# ---------- Example usage ----------
if __name__ == "__main__":
    arr = [45, 3, 22, 18, 5, 73, 61, 38, 11, 8, 92, 14, 29, 41, 2, 77]
    sorted_arr = bitonic_sort(arr, up=True)
    print("Sorted array:", sorted_arr)
