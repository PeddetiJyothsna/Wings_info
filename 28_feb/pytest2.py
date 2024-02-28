import pytest
from pytest1 import square

def test_positive():
    assert square(2)==4
    assert square(3)==9
def test_negative():
    assert square(-2) ==4
    assert square(-3)==9
def test_zero():
    assert square(0)==0
def test_string1():
    with pytest.raises(TypeError):
        square("cat")


"""
pytest2.py FF.F                                                                                                                                            [100%]

=========================================================================== FAILURES ============================================================================ 
_________________________________________________________________________ test_positive _________________________________________________________________________ 

    def test_positive():
        assert square(2)==4
>       assert square(3)==9
E       assert 6 == 9
E        +  where 6 = square(3)

pytest2.py:5: AssertionError
_________________________________________________________________________ test_negative _________________________________________________________________________ 

    def test_negative():
>       assert square(-2) ==4
E       assert -4 == 4
E        +  where -4 = square(-2)

pytest2.py:7: AssertionError
_________________________________________________________________________ test_string1 __________________________________________________________________________ 

    def test_string1():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytest2.py:12: Failed
==================================================================== short test summary info ==================================================================== 
FAILED pytest2.py::test_positive - assert 6 == 9
FAILED pytest2.py::test_negative - assert -4 == 4
FAILED pytest2.py::test_string1 - Failed: DID NOT RAISE <class 'TypeError'>
================================================================== 3 failed, 1 passed in 0.13s ================================================================== 
"""