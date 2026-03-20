import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from algorithms.jump_search import jump_search


def test_jump_search_found():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert jump_search(arr, 6) == 5


def test_jump_search_first_element():
    arr = [10, 20, 30]
    assert jump_search(arr, 10) == 0


def test_jump_search_not_found():
    arr = [1, 3, 5, 7]
    assert jump_search(arr, 2) == -1


def test_jump_search_empty():
    arr = []
    assert jump_search(arr, 1) == -1
