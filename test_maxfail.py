import pytest
import math

#execution will stop after 2 test failures  >> pytest test_maxfail.py --maxfail 2
def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 40

def test_equality_failure():
   assert 10 == 11