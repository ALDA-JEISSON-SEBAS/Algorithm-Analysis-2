import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from algorithms.interpolation_search import interpolation_search


def test_interpolation_search_found():
    arr = [10, 20, 30, 40, 50]
    assert interpolation_search(arr, 40) == 3


def test_interpolation_search_first():
    arr = [5, 10, 15, 20]
    assert interpolation_search(arr, 5) == 0


def test_interpolation_search_not_found():
    arr = [1, 2, 3, 4, 5]
    assert interpolation_search(arr, 100) == -1


def test_interpolation_search_single():
    arr = [42]
    assert interpolation_search(arr, 42) == 0
