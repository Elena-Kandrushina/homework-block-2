import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def test1_get_mask_card_number() -> list:
    return "1234567891234567"
def test_get_mask_card_number(test1_get_mask_card_number):
    assert get_mask_card_number(test1_get_mask_card_number) == "1234 56 ** **** 4567"


def test2_get_mask_card_number() -> None:
    assert get_mask_card_number("120000034567891234567") == "Введен некорректный номер"


#with pytest.raises(ValueError) as exc_info:
    #get_mask_card_number("aaaa1111bbbb2222") == "ValueError: Введен некорректный номер"


@pytest.mark.parametrize(
    "card_number, expected",
    [("1234567891234567", "1234 56 ** **** 4567"), ("7700567891234555", "7700 56 ** **** 4555")],
)
def test_4_get_mask_card_number(card_number: str, expected: str) -> None:
    assert len(card_number) + 4 == len(expected)


@pytest.mark.parametrize("card_number, expected", [("1234567890123456", "1234 56 ** **** 3456")])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [("1277777722222", "**2222")])
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected

