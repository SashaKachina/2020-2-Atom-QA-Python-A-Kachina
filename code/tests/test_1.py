import pytest


def test1():
    a = [1, 2, 3]
    a.pop()
    assert a == [1, 2]
def test2():
    a = [1, 2, 3]
    b = len(a)
    a.append(4)
    assert len(a) != b
def test3():
    a = [1, 2, 3]
    a.clear()
    assert len(a) == 0

@pytest.mark.parametrize ('i', list(range(10)))
def test4(i):
    assert i < 10

class TestClass:
    def test5(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        assert a == b