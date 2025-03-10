import pytest
from program import divide_numbers, reverse_string, get_list_element

def test_divide_numbers():
    # Normal test case:
    assert divide_numbers(10, 2) == 5.00

    # Edge case:
    assert divide_numbers(0.01, 10) == 0.001

    # Corner case:
    assert divide_numbers(10, 0) == 0

def test_reverse_string():
    # Normal test case:
    assert reverse_string("tacocat") == "TACOCAT"

    # Edge case (32-characters of mixed case):
    assert reverse_string("nMLkJiHgFeDcBAzYxWvUtSrQpNmLkDbA") == "aBdKlMnPqRsTuVwXyZabCdEfGhIjKlmN"

    # Corner case:
    assert reverse_string("Y33T") == "t33y"

def test_get_list_element():

    # Normal test case:
    assert get_list_element("tacocat", 0) == "t"

    # Edge case:
    assert get_list_element("tacocat", 7) == "t"

    # Corner case:
    assert get_list_element("tacocat", 99) == ""