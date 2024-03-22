# test_factorial.py
import pytest
from factorial import factorial

# def test_factorial_negative_input():
#     with pytest.raises(ValueError):
#         factorial(-1)
        
def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1
    
def test_factorial_positive_input():
    assert factorial(5) == 120

def test_factorial_positive_input_1():
    assert factorial(4) == 24

def test_factorial_positive_input_2():
    assert factorial(3) == 6
    
def test_factorial_large_input():
    assert factorial(30) == 265252859812191058636308480000000  