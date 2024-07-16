from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> str:
    """Функция маскирует номер карты или счета."""
    if "Счет" or "Счёт" or "счет" or "счёт" in string:
        account = get_mask_account(string[-20:])
        mask_account = string.replace(string[-20:], account)
        return mask_account
    else:
        card = get_mask_card_number(string[-16:])
        mask_card = string.replace(string[-16:], card)
        return card


def get_data(data: str) -> str:
    """Функция, которая возвращает строку с датой в требуемом формате."""
    d = datetime.strptime(data, format("%Y-%m-%dt%H:%M:%S.%f"))
    return d.strftime("%d.%m.%Y")

if __name__ == "__main__":
    print(mask_account_card("Visa platinum 1111222233334444"))
    print(mask_account_card("Счет 11112222333344445555"))
    print(get_data("2018-07-11T02:26:18.671407"))
