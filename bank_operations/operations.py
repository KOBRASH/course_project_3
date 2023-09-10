def filter_executed_operations(operations):
    """
    Фильтрация выполненных операций.

    Args:
        operations (list): Список операций.

    Returns:
        list: Список выполненных операций.
    """
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    return executed_operations

def sort_operations_by_date(operations):
    """
    Сортировка операций по дате (убывающая).

    Args:
        operations (list): Список операций.

    Returns:
        list: Отсортированный список операций.
    """
    sorted_operations = sorted(operations, key=lambda op: op['date'], reverse=True)
    return sorted_operations
