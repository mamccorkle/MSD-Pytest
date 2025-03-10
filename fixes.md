# Testing Errors:

```
PS C:\Users\Instructor\Code\Python\MSD-Pytest> pytest test_program.py
=============================================================================== test session starts ===============================================================================
platform win32 -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\Users\Instructor\Code\Python\MSD-Pytest
collected 3 items                                                                                                                                                                  

test_program.py F.F                                                                                                                                                          [100%]

==================================================================================== FAILURES =====================================================================================
_______________________________________________________________________________ test_divide_numbers _______________________________________________________________________________

    def test_divide_numbers():
        # Normal test case:
        assert divide_numbers(10, 2) == 5.00
    
        # Edge case:
>       assert divide_numbers(0.01, 10) == 0.001
E       assert 0.0 == 0.001
E        +  where 0.0 = divide_numbers(0.01, 10)

test_program.py:9: AssertionError
______________________________________________________________________________ test_get_list_element ______________________________________________________________________________

    def test_get_list_element():
    
        # Normal test case:
        assert get_list_element("tacocat", 0) == "t"

        # Edge case:
>       assert get_list_element("tacocat", 7) == "t"
E       AssertionError: assert 'Not found' == 't'
E
E         - t
E         + Not found

test_program.py:30: AssertionError
============================================================================= short test summary info ============================================================================= 
FAILED test_program.py::test_divide_numbers - assert 0.0 == 0.001
FAILED test_program.py::test_get_list_element - AssertionError: assert 'Not found' == 't'
=========================================================================== 2 failed, 1 passed in 0.10s =========================================================================== 
PS C:\Users\Instructor\Code\Python\MSD-Pytest> 
```

<img src="https://github.com/mamccorkle/MSD-Pytest/blob/main/failtest1.png">

# The fix:

## fixed_divide_numbers():

> With this function, we needed to raise a pytest ZeroDivisionError then fix the bug as noted below:
> 
>    with pytest.raises(ZeroDivisionError) as excinfo:
>        fixed_divide_numbers(10, 0)
>    assert str(excinfo.value) == "Division by zero is not allowed"

## fixed_reverse_string():

> With this function we needed to raise a pytest TypeError then fix the bug as noted below:
> 
>    with pytest.raises(TypeError) as excinfo:
>        fixed_reverse_string("Y33T!")
>    assert str(excinfo.value) == "Invalid character"

## fixed_get_list_element():

> With this function, we needed to raise a pytest IndexError then fix the bug as noted below:
> 
>    with pytest.raises(IndexError) as excinfo:
>        fixed_get_list_element("tacocat", 99)
>    assert str(excinfo.value) == "Not found, index is out of bounds"

<img src="https://github.com/mamccorkle/MSD-Pytest/blob/main/proof.png">