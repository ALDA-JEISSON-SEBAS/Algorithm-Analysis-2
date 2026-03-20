def binary_search(arr, target):
    """
    Binary Search Algorithm

    Description:
    Repeatedly divides the sorted array in half to locate the target.

    Time Complexity:
        Best / Average / Worst: O(log n)

    Space Complexity:
        O(1)
    """

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
