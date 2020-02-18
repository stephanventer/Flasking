import pytest
import example

def test_function1_test1():
    assert example.function_1(3) == 5, "Calculation incorrect"

def test_function1_test2():
    assert example.function_1(-3) == -27, "Result cannot be negative"

def test_function1_test3():
    assert example.function_1(-3) == 27, "Success"