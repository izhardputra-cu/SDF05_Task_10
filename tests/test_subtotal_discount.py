import pytest

from pricing import apply_member_discount, calculate_subtotal


@pytest.mark.parametrize(
    "unit_price, quantity, expected",
    [(100, 2, 200), (12500, 3, 37500), (19.99, 3, 59.97)],
)
def test_subtotal(unit_price, quantity, expected):
    assert calculate_subtotal(unit_price, quantity) == pytest.approx(expected)


def test_subtotal_zero_price():
    assert calculate_subtotal(0, 3) == 0


def test_subtotal_negative_price():
    with pytest.raises(ValueError, match="unit_price must not be negative"):
        calculate_subtotal(-1, 2)


@pytest.mark.parametrize("quantity", [0, -1, -5])
def test_subtotal_invalid_quantity(quantity):
    with pytest.raises(ValueError, match="quantity must be positive"):
        calculate_subtotal(100, quantity)


@pytest.mark.parametrize(
    "subtotal, is_member, expected",
    [(200, True, 180), (200, False, 200),
     (59.97, True, 53.973), (0, True, 0), (0, False, 0)],
)
def test_member_discount(subtotal, is_member, expected):
    assert apply_member_discount(subtotal, is_member) == pytest.approx(expected)
