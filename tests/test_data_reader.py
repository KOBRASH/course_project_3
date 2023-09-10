# test_data_reader.py
import json
import pytest
from bank_operations.data_reader import read_operations_data

# Создаем временный JSON-файл с данными для тестов
@pytest.fixture
def sample_data_file(tmp_path):
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
    ]
    data_file = tmp_path / "sample_data.json"
    with open(data_file, 'w') as file:
        json.dump(data, file)
    return data_file

# Тест для функции read_operations_data
def test_read_operations_data(sample_data_file):
    # Чтение данных из временного файла
    data = read_operations_data(sample_data_file)

    # Проверка, что данные считаны успешно
    assert len(data) == 2
    assert data[0]["state"] == "EXECUTED"
    assert data[1]["state"] == "CANCELED"
