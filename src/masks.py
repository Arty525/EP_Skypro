def get_mask_card_number(num: str) -> str:
    """
    :param num: номер карты из main.py
    Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX
    где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры,
    разделенным пробелами.
    Пример работы функции:
        7000792289606361 - входной аргумент
        7000 79** **** 6361 - выход функции
    """
    return f"{num[:4]} {num[4:6]}** **** {num[-4:]}"


def get_mask_account(num: str) -> str:
    """
    :param num: номер карты из main.py
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX
    где X — это цифра номера. То есть видны только последние 4 цифры номера,
    а перед ними — две звездочки.
    Пример работы функции:
        73654108430135874305 - входной аргумент
        **4305 - выход функции
    """
    return "**" + num[-4:]
