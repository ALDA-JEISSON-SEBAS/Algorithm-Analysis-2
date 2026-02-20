def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm

    Description:
    Estimates position based on value distribution.
    Works best on uniformly distributed sorted arrays.

    Average Case: O(log log n)
    Worst Case: O(n)
    """

    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:

        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + int(
            ((float(high - low) / (arr[high] - arr[low]))
             * (target - arr[low]))
        )

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1