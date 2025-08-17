import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum  700 07 ** **** 0636"),
        ("Maestro 7000792289606361", "Maestro  700 07 ** **** 0636"),
        ("Счет 73654108430135874305", "Счет **7430"),
    ],
)
def test_mask_account_card(account_card: str, expected: str) -> None:
    assert mask_account_card(account_card) == expected


@pytest.fixture
def test_1_get_date() -> str:
    return "2025-07-20T02:26:18.671407"


def test_get_dare(test_1_get_date):
    assert get_date(test_1_get_date) == "20-07-2025"
