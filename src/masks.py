import logging


logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
     XXXX XX** **** XXXX"""

    card_number = str(card_number)

    if len(card_number) == 16:
        logger.info("Введен корректный номер")
        mask_card_number = f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"
        logger.info("Номер маскирован")
        return mask_card_number
    logger.error("Введен некорректный номер")

    return "Введен некорректный номер"


if __name__ == "__main__":
    print(get_mask_card_number("1234567891234567"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX"""

    account_number = str(account_number)
    if len(account_number) >= 4:
        logger.info("Введен корректный номер")
        mask_account_number = f"**{account_number[-4:]}"
        logger.info("Номер маскирован")

        return mask_account_number
    logger.error("Введен некорректный номер")
    return "Введен некорректный номер"


if __name__ == "__main__":
    print(get_mask_account("1277777722222"))
