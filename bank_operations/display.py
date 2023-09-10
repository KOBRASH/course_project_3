def display_operations(operations):
    for operation in operations:
        date = operation['date']  # Получаем дату из данных операции
        formatted_date = format_date(date)  # Форматируем дату в требуемый формат
        description = operation['description']
        from_account = mask_card_number(operation.get('from', ''))
        to_account = mask_account_number(operation['to'])
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        # Формируем строку вывода
        output = f"{formatted_date} {description}\n{from_account} -> {to_account}\n{amount} {currency}\n"
        print(output)

def format_date(date_str):
    # Преобразование даты из "ГГГГ-ММ-ДД" в "ДД.ММ.ГГГГ"
    parts = date_str.split('-')
    return f"{parts[2]}.{parts[1]}.{parts[0]}"

def mask_card_number(card_number):
    # Маскирование номера карты
    if card_number:
        masked_number = card_number[:4] + ' **** **** ' + card_number[-4:]
        return masked_number
    return ''

def mask_account_number(account_number):
    # Маскирование номера счета
    if account_number:
        masked_number = '**' + account_number[-4:]
        return masked_number
    return ''
