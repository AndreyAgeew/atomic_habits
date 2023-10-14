from django.db import models

from users.models import User


class Habit(models.Model):
    """
    Модель, представляющая собой привычку пользователя.

    Поля:
    - user (ForeignKey): Пользователь, создавший привычку.
    - place (CharField): Место, в котором необходимо выполнять привычку.
    - time (TimeField): Время, когда необходимо выполнять привычку.
    - action (CharField): Действие, которое представляет из себя привычку.
    - is_reward (BooleanField): Признак приятной привычки.
    - related_habit (ForeignKey): Связанная привычка, если таковая имеется.
    - frequency (CharField): Периодичность выполнения привычки для напоминания в днях.
    - reward (CharField): Вознаграждение за выполнение привычки.
    - estimated_time (IntegerField): Время, которое предположительно потратит пользователь на выполнение привычки.
    - is_public (BooleanField): Признак публичности привычки.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, help_text="Место, в котором необходимо выполнять привычку.")
    time = models.TimeField(help_text="Время, когда необходимо выполнять привычку.")
    action = models.CharField(max_length=255, help_text="Действие, которое представляет из себя привычку.")
    is_reward = models.BooleanField(default=False, help_text="Признак приятной привычки.")
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                      help_text="Связанная привычка, если таковая имеется.")
    frequency = models.CharField(max_length=255, default='daily',
                                 help_text="Периодичность выполнения привычки для напоминания в днях.")
    reward = models.CharField(max_length=255, help_text="Вознаграждение за выполнение привычки.")
    estimated_time = models.IntegerField(
        help_text="Время, которое предположительно потратит пользователь на выполнение привычки.")
    is_public = models.BooleanField(default=False, help_text="Признак публичности привычки.")
