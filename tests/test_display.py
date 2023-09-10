import pytest
from bank_operations.display import display_operations, format_date, mask_card_number, mask_account_number

# Тесты для функции format_date
def test_format_date():
    # Проверяем, что функция корректно форматирует дату
    input_date = "2023-09-01"
    expected_output = "01.09.2023"
    assert format_date(input_date) == expected_output

# Тесты для функции mask_card_number
def test_mask_card_number():
    # Проверяем, что функция корректно маскирует номер карты
    card_number = "1234567890123456"
    expected_output = "1234 **** **** 3456"
    assert mask_card_number(card_number) == expected_output

    # Проверяем, что функция корректно обрабатывает пустой номер карты
    empty_card_number = ""
    assert mask_card_number(empty_card_number) == ""

# Тесты для функции mask_account_number
def test_mask_account_number():
    # Проверяем, что функция корректно маскирует номер счета
    account_number = "9876543210"
    expected_output = "**3210"
    assert mask_account_number(account_number) == expected_output

    # Проверяем, что функция корректно обрабатывает пустой номер счета
    empty_account_number = ""
    assert mask_account_number(empty_account_number) == ""

# Тест для функции display_operations
def test_display_operations(capsys):
    # Подготавливаем тестовые данные
    operations = [
        {
            "date": "2023-09-01T10:00:00",
            "description": "Перевод организации",
            "from": "1234567890",
            "to": "9876543210",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "руб."}},
        }
    ]

    # Запускаем функцию display_operations
    display_operations(operations)

    # Проверяем, что вывод соответствует ожиданиям
    captured = capsys.readouterr()
    expected_output = (
        "01T10:00:00.09.2023 Перевод организации\n"
        "1234 **** **** 7890 -> **3210\n"
        "1000.00 руб.\n\n"
    )
    assert captured.out == expected_output
