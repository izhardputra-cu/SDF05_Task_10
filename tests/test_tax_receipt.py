import pytest

from pricing import add_tax, write_receipt


@pytest.mark.parametrize(
    "amount, expected", [(100, 111), (180, 199.8), (53.973, 59.91003)],
)
def test_add_tax(amount, expected):
    assert add_tax(amount) == pytest.approx(expected)


def test_add_tax_zero():
    assert add_tax(0) == pytest.approx(0)


def test_receipt_single_line(tmp_path):
    receipt = tmp_path / "receipt.txt"
    write_receipt(receipt, ["Total: 111"])
    assert receipt.read_text(encoding="utf-8") == "Total: 111\n"


def test_receipt_multiple_lines(tmp_path):
    receipt = tmp_path / "receipt.txt"
    write_receipt(receipt, ["Kafé", "Subtotal: 100", "Total: 111"])
    assert receipt.read_text(encoding="utf-8") == "Kafé\nSubtotal: 100\nTotal: 111\n"


def test_receipt_empty_lines(tmp_path):
    receipt = tmp_path / "receipt.txt"
    write_receipt(receipt, [])
    assert receipt.read_text(encoding="utf-8") == "\n"
