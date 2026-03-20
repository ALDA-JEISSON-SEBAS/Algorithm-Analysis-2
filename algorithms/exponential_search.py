from algorithms.binary_search import binary_search

def exponential_search(arr, target):
    """
    Exponential Search Algorithm

    Description:
    Finds range exponentially, then applies binary search.

    Time Complexity:
        O(log n)
    """

    if not arr:
        return -1

    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1

    while i < n and arr[i] <= target:
        i *= 2

    left = i // 2
    right = min(i, n)
    result = binary_search(arr[left:right], target)
    if result == -1:
        return -1
    return left + result
