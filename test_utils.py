from utils import add, kurang


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_kurang():
    assert kurang(5, 3) == 2


def test_kurang_negative():
    assert kurang(-1, 1) == -2
