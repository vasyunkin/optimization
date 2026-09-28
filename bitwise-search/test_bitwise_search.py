import pytest

from third import bitwise_search


def test_minimum_at_left_boundary():
    f = lambda x: (x + 2) ** 2

    result = bitwise_search(f, -2, 5)

    assert result == pytest.approx(-2, abs=1e-4)


def test_minimum_at_right_boundary():
    f = lambda x: (x - 5) ** 2

    result = bitwise_search(f, -2, 5)

    assert result == pytest.approx(5, abs=1e-4)


def test_both_boundaries_are_minimum():
    f = lambda x: (x + 2) ** 2 * (x - 5) ** 2

    result = bitwise_search(f, -2, 5)

    assert result == pytest.approx(-2, abs=1e-4) or \
           result == pytest.approx(5, abs=1e-4)


def test_minimum_inside_interval():
    f = lambda x: (x - 3) ** 2

    result = bitwise_search(f, 0, 10)

    assert result == pytest.approx(3, abs=1e-4)


def test_constant_function():
    f = lambda x: 7

    result = bitwise_search(f, -2, 5)

    assert -2 <= result <= 5