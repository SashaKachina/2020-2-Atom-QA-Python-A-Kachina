import pytest
import random

@pytest.fixture()
def random_value():
        print('entering')
        yield random.randint(1,1000)
        print('exiting')
