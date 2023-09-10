import json

def read_operations_data(file_path):
    """
    Чтение данных из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        list: Список операций из JSON.
    """
    with open(file_path, 'r') as file:
        operations_data = json.load(file)
    return operations_data
