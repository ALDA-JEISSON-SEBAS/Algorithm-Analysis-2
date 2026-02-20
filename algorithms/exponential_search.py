from algorithms.binary_search import binary_search

def exponential_search(arr, target):
    """
    Exponential Search Algorithm

    Description:
    Finds range exponentially, then applies binary search.

    Time Complexity:
        O(log n)
    """

    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1

    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr[:min(i, n)], target)