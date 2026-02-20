import math

def jump_search(arr, target):
    """
    Jump Search Algorithm

    Description:
    Jumps ahead by fixed steps and then performs linear search in the block.

    Time Complexity:
        O(√n)

    Space Complexity:
        O(1)
    """

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1