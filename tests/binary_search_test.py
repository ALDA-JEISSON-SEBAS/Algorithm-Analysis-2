import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from algorithms.binary_search import binary_search


def test_binary_search_found_middle():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2


def test_binary_search_found_last():
    arr = [2, 4, 6, 8]
    assert binary_search(arr, 8) == 3


def test_binary_search_not_found():
    arr = [1, 2, 3, 4]
    assert binary_search(arr, 10) == -1


def test_binary_search_single_element():
    arr = [100]
    assert binary_search(arr, 100) == 0
