from rest_framework import serializers


def validate_related_habit(value):
    """
    Валидатор: Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """
    if value.related_habit and value.reward:
        raise serializers.ValidationError("You can't choose both a related habit and a reward.")


def validate_estimated_time(value):
    """
    Валидатор: Время выполнения должно быть не больше 120 секунд.
    """
    if value.estimated_time > 120:
        raise serializers.ValidationError("Estimated time should not exceed 120 seconds.")


