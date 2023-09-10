# test_operations.py
import pytest
from bank_operations.operations import filter_executed_operations, sort_operations_by_date

# Тест для функции filter_executed_operations
def test_filter_executed_operations():
    data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-09-01T10:00:00",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-09-02T12:00:00",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-09-03T14:00:00",
        },
    ]
    filtered_data = filter_executed_operations(data)
    assert len(filtered_data) == 2
    assert filtered_data[0]["state"] == "EXECUTED"
    assert filtered_data[1]["state"] == "EXECUTED"

# Тест для функции sort_operations_by_date
def test_sort_operations_by_date():
    data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-09-01T10:00:00",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-09-02T12:00:00",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2023-09-03T14:00:00",
        },
    ]
    sorted_data = sort_operations_by_date(data)
    assert sorted_data[0]["id"] == 3
    assert sorted_data[1]["id"] == 2
    assert sorted_data[2]["id"] == 1
