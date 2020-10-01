import pytest

def test1():
    s = 'Hello, my dear friend'
    assert len(s) == 21

def test2():
    s1 = "Hello,"
    s2 = " world!"
    assert s1 + s2 == "Hello, world!"

def test3():
    s = 'hello'
    assert s[-4] == 'e'

@pytest.mark.parametrize('i',{'o','p','u'})
def test4(i):
    assert len(i) == 1

class TestClass:
    def test5(self):
        s = 'string'
        a = s.find('i')
        assert a == 3