from algorithms.linear_search import linear_search


def test_linear_search_found_middle():
    arr = [10, 20, 30, 40, 50]
    assert linear_search(arr, 30) == 2


def test_linear_search_found_first():
    arr = [5, 10, 15]
    assert linear_search(arr, 5) == 0


def test_linear_search_not_found():
    arr = [1, 2, 3]
    assert linear_search(arr, 10) == -1


def test_linear_search_empty():
    arr = []
    assert linear_search(arr, 5) == -1