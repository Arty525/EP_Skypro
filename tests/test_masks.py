import pytest

import src.masks as masks


#Тестирование функции get_mask_card_number из модуля src/masks.py
@pytest.fixture
def card_number():
    return "7000792289606361"

def test_mask_card_number(card_number):
    assert masks.get_mask_card_number(card_number) == "7000 79** **** 6361"


#Тестирование функции get_mask_account из модуля src/masks.py
@pytest.fixture
def account():
    return "73654108430135874305"

def test_mask_account(account):
    assert masks.get_mask_account(account) == "**4305"