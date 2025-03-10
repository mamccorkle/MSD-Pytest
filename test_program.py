import pytest
from program import divide_numbers, reverse_string, get_list_element, fixed_divide_numbers, fixed_reverse_string, fixed_get_list_element

def test_divide_numbers():
    # # Normal test case:
    # assert divide_numbers(10, 2) == 5.00
    #
    # # Edge case:
    # assert divide_numbers(0.01, 10) == 0.001
    #
    # # Corner case:
    # assert divide_numbers(10, 0) == 0

# FIXED:

    # Normal test case:
    assert fixed_divide_numbers(10, 2) == 5.00

    # Edge case:
    assert fixed_divide_numbers(0.01, 10) == 0.001

    # Corner case:
    with pytest.raises(ZeroDivisionError) as excinfo:
        fixed_divide_numbers(10, 0)
    assert str(excinfo.value) == "Division by zero is not allowed"


def test_reverse_string():
    # # Normal test case:
    # assert reverse_string("tacocat") == "TACOCAT"
    #
    # # Edge case (32-characters of mixed case):
    # assert reverse_string("nMLkJiHgFeDcBAzYxWvUtSrQpNmLkDbA") == "aBdKlMnPqRsTuVwXyZabCdEfGhIjKlmN"
    #
    # # Corner case:
    # assert reverse_string("Y33T!") == "!t33y"

# FIXED:

    # Normal test case:
    assert fixed_reverse_string("tacocat") == "TACOCAT"

    # Edge case (32-characters of mixed case):
    assert fixed_reverse_string("nMLkJiHgFeDcBAzYxWvUtSrQpNmLkDbA") == "aBdKlMnPqRsTuVwXyZabCdEfGhIjKlmN"

    # Corner case:
    with pytest.raises(TypeError) as excinfo:
        fixed_reverse_string("Y33T!")
    assert str(excinfo.value) == "Invalid character"

def test_get_list_element():
    # # Normal test case:
    # assert get_list_element("tacocat", 0) == "t"
    #
    # # Edge case:
    # assert get_list_element("tacocat", 7) == "t"
    #
    # # Corner case:
    # assert get_list_element("tacocat", 99) == ""

# FIXED:

    # Normal test case:
    assert fixed_get_list_element("tacocat", 0) == "t"

    # Edge case:
    assert fixed_get_list_element("tacocat", 6) == "t"

    # Corner case:
    with pytest.raises(IndexError) as excinfo:
        fixed_get_list_element("tacocat", 99)
    assert str(excinfo.value) == "Not found, index is out of bounds"


