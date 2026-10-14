import pytest

from pricing import calculate_total


@pytest.mark.parametrize(
    "unit_price, quantity, expected",
    [(100, 1, 99.9), (12500, 2, 24975), (19.99, 3, 59.91003)],
)
def test_total_member(unit_price, quantity, expected):
    assert calculate_total(unit_price, quantity, True) == pytest.approx(expected)


def test_total_non_member():
    assert calculate_total(12500, 2, False) == pytest.approx(27750)
    assert calculate_total(12500, 2) == pytest.approx(27750)


@pytest.mark.parametrize("is_member", [True, False])
def test_total_zero_price(is_member):
    assert calculate_total(0, 3, is_member) == pytest.approx(0)


@pytest.mark.parametrize(
    "unit_price, quantity, message",
    [(-1, 1, "unit_price must not be negative"),
     (100, 0, "quantity must be positive"),
     (100, -2, "quantity must be positive")],
)
def test_total_invalid_input(unit_price, quantity, message):
    with pytest.raises(ValueError, match=message):
        calculate_total(unit_price, quantity)
