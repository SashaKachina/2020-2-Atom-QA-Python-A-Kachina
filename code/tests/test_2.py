import pytest

def test1():
    set = {'h','e','l','l','o'}
    with pytest.raises(AssertionError):
        assert 'i' in set
def test2():
    set_1 = {'h','e','l','l','o'}
    set_2 = {'b', 'y', 'e'}
    assert set_1.isdisjoint(set_2) != True

def test3():
    set_1 = {'h','1','e','2'}
    set_2 = {'e','h','2','1'}
    assert set_1 == set_2

@pytest.mark.parametrize('i', {1,3,5,7,9})
def test4(i):
    assert i % 2 != 0

class TestClass:
    def test5(self):
        set_1 = {1,2,3,4}
        set_2 = {1,2,5,6}
        set_3 = {1,2,3,4,5,6,1,2}
        set_1.update(set_2)
        assert set_1 == set_3

