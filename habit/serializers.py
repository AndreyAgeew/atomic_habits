from rest_framework import serializers

from habit.models import Habit
from habit.validators import validate_related_habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habit.
    """

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        Валидаторы для модели Habit.
        """
        validate_related_habit(data)

