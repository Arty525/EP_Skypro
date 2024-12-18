import pytest

import src.masks as masks

#Тестирование функции get_mask_card_number из модуля src/masks.py
@pytest.mark.parametrize("value, expected", [("7000792289606361", "7000 79** **** 6361")])
def test_get_mask_card_number(value, expected):
    assert masks.get_mask_card_number(value) == expected


#Тестирование функции get_mask_account
@pytest.mark.parametrize("value, expected", [("73654108430135874305","**4305")])
def test_get_mask_account(value, expected):
    assert masks.get_mask_account(value) == expected