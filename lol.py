import pytest
def func(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
def test_method():
    assert func(3) =="odd"
def test_method1():
    assert func(10)== "odd"
@pytest.mark.varun
def test_case():
    assert func(12)=="even"