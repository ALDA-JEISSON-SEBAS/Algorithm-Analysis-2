def linear_search(arr, target):
    """
    Linear Search Algorithm

    Description:
    Iterates through the list sequentially until the target is found.

    Time Complexity:
        Best Case: O(1)
        Average Case: O(n)
        Worst Case: O(n)

    Space Complexity:
        O(1)
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1