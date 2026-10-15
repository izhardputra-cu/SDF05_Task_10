import pytest

from pricing import apply_member_discount, calculate_subtotal


@pytest.mark.parametrize(
    "unit_price, quantity, expected",
    [(100, 1, 100), (12500, 2, 25000), (19.99, 3, 59.97)],
)
def test_subtotal_valid(unit_price, quantity, expected):
    assert calculate_subtotal(unit_price, quantity) == pytest.approx(expected)


def test_subtotal_zero_price():
    assert calculate_subtotal(0, 5) == 0


@pytest.mark.parametrize(
    "unit_price, quantity, message",
    [(-1, 1, "unit_price must not be negative"),
     (100, 0, "quantity must be positive"),
     (100, -3, "quantity must be positive")],
)
def test_subtotal_invalid_input(unit_price, quantity, message):
    with pytest.raises(ValueError, match=message):
        calculate_subtotal(unit_price, quantity)


@pytest.mark.parametrize(
    "subtotal, expected", [(100, 90), (25000, 22500), (59.97, 53.973)],
)
def test_discount_member(subtotal, expected):
    assert apply_member_discount(subtotal, True) == pytest.approx(expected)


@pytest.mark.parametrize("subtotal", [100, 25000, 59.97])
def test_discount_non_member(subtotal):
    assert apply_member_discount(subtotal, False) == pytest.approx(subtotal)


@pytest.mark.parametrize("is_member", [True, False])
def test_discount_zero_subtotal(is_member):
    assert apply_member_discount(0, is_member) == pytest.approx(0)
