from datetime import time

import pytest
from rest_framework.exceptions import ValidationError

from habit.validators import (
    validate_estimated_time,
    validate_frequency,
    validate_notification_time,
    validate_related_habit,
    validate_rewarding_habit,
)


def test_validate_related_habit():
    valid_data = {"related_habit": None, "reward": ""}
    validate_related_habit(valid_data)  # Не должно вызывать ошибку

    invalid_data = {"related_habit": 1, "reward": "Тестовая награда"}
    with pytest.raises(ValidationError):
        validate_related_habit(invalid_data)


def test_validate_estimated_time():
    valid_data = {"estimated_time": 60}
    validate_estimated_time(valid_data)  # Не должно вызывать ошибку

    invalid_data = {"estimated_time": 150}
    with pytest.raises(ValidationError):
        validate_estimated_time(invalid_data)


def test_validate_rewarding_habit():
    valid_data = {"is_reward": True, "reward": "", "related_habit": None}
    validate_rewarding_habit(valid_data)  # Не должно вызывать ошибку

    invalid_data = {
        "is_reward": True,
        "reward": "Тестовая награда",
        "related_habit": None,
    }
    with pytest.raises(ValidationError):
        validate_rewarding_habit(invalid_data)


def test_validate_frequency():
    valid_data = {"frequency": "daily"}
    validate_frequency(valid_data)  # Не должно вызывать ошибку

    invalid_data = {"frequency": "monthly"}
    with pytest.raises(ValidationError):
        validate_frequency(invalid_data)


def test_validate_notification_time():
    valid_data = {
        "frequency": "daily",
        "notification_time": "thirty",
        "time": time(12, 0, 0),  # Преобразование строки времени в объект datetime.time
    }

    # Убедится, что при правильных данных валидатор не вызывает исключение
    try:
        validate_notification_time(valid_data)
    except ValidationError:
        pytest.fail("validate_notification_time raised ValidationError for valid data.")

    invalid_data = {
        "frequency": "weekly",
        "notification_time": "day",
        "time": time(12, 0, 0),  # Преобразование строки времени в объект datetime.time
    }

    # Убедится, что при неверных данных валидатор вызывает исключение
    with pytest.raises(ValidationError):
        validate_notification_time(invalid_data)
