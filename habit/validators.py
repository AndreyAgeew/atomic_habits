from rest_framework import serializers


def validate_related_habit(value):
    """
    Валидатор: Исключить одновременный выбор связанной привычки и указания вознаграждения.
    """
    if value.related_habit and value.reward:
        raise serializers.ValidationError("You can't choose both a related habit and a reward.")



