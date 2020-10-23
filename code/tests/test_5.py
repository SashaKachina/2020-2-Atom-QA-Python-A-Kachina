import pytest
import random


def test1():
    a = 60
    b = 7
    assert a % b == 4


def test2():
    with pytest.raises(ZeroDivisionError):
        assert 50 / 0


def test3():
    a = 5
    b = 4
    assert a - b == 1


@pytest.mark.parametrize('i', list(range(5)))
def test4(i):
    i = i + 1
    assert -i < 0


class TestClass:
    def test5(self):
        random_value = random.randint(1,100)
        assert random_value < 100
