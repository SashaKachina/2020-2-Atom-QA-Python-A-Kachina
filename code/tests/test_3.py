import pytest


def test1():
    dictionary = {'a' : '1','b' : '2', 'c' : '3'}
    dictionary['a'] = '4'
    assert dictionary['a'] != '1'

def test2():
    dictionary = {a: a ** 2 for a in range(7)}
    assert dictionary[6] == 36

def test3():
    dictionary = {1:1}
    assert dictionary.copy() != 0

@pytest.mark.parametrize('i', {'a' : 1, 'b' : 2, 'c' : 3})
def test4(i):
    assert i in ('a','b','c')

class TestClass:
    def test5(self):
        dictionary = {'маша' : 50, 'саша' : 16, 'паша': 34}
        dictionary.clear()
        assert dictionary == {}
