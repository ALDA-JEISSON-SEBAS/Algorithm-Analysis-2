from algorithms.exponential_search import exponential_search


def test_exponential_search_found():
    arr = [2, 4, 6, 8, 10, 12]
    assert exponential_search(arr, 8) == 3


def test_exponential_search_first():
    arr = [1, 3, 5, 7]
    assert exponential_search(arr, 1) == 0


def test_exponential_search_not_found():
    arr = [10, 20, 30]
    assert exponential_search(arr, 25) == -1


def test_exponential_search_single():
    arr = [99]
    assert exponential_search(arr, 99) == 0