import pytest

from src.widget import *


#Тестирование функции mask_account_card из модуля src/widget.py
@pytest.mark.parametrize("value, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


#Тестирование функции get_date из модуля src/widget.py
@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"

def test_get_date(date):
    assert get_date(date) == "11.03.2024"
