from bank_operations.data_reader import read_operations_data
from bank_operations.operations import filter_executed_operations, sort_operations_by_date
from bank_operations.display import display_operations

def main():
    # Чтение данных из файла
    operations_data = read_operations_data('operations.json')

    # Фильтрация и сортировка операций
    executed_operations = filter_executed_operations(operations_data)
    sorted_operations = sort_operations_by_date(executed_operations)

    # Вывод последних 5 операций
    display_operations(sorted_operations[:5])

if __name__ == "__main__":
    main()
