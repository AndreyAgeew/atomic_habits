from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from habit.models import Habit
from datetime import datetime, timedelta


def _check_starting(habit, current_day):
    """
    Проверяет, начинается ли привычка сегодня или завтра, и устанавливает флаг `is_starting` в True, если так.

    :param habit: Привычка для проверки
    :param current_day: Текущий день
    """
    if not habit.is_starting:
        if habit.weekday == 'today':
            habit.is_starting = True
        elif habit.weekday == 'tomorrow' and current_day == habit.date_of_start.day + 1:
            habit.is_starting = True
        habit.save()


def _check_frequency_weekly(habit):
    """
    Обновляет дату начала привычки в зависимости от выбранной частоты (ежедневно или еженедельно).

    :param habit: Привычка, для которой обновляется дата начала
    """
    if habit.frequency == 'weekly':
        habit.date_of_start += timedelta(days=7)
    else:
        habit.date_of_start += timedelta(days=1)
    habit.save()


def _get_mailing_time(habit):
    """
    Возвращает день, час и минуту для отправки уведомления о привычке.

    :param habit: Привычка для которой вычисляется время уведомления
    :return: Кортеж (день, час, минута)
    """
    mailing_date = datetime.combine(habit.date_of_start, habit.time)

    if habit.notification_time == 'fifteen':
        mailing_date -= timedelta(minutes=15)
    elif habit.notification_time == 'thirty':
        mailing_date -= timedelta(minutes=30)
    elif habit.notification_time == 'hour':
        mailing_date -= timedelta(hours=1)
    elif habit.notification_time == 'two_hours':
        mailing_date -= timedelta(hours=2)
    else:
        mailing_date -= timedelta(days=1)

    return mailing_date.day, mailing_date.hour, mailing_date.minute


@shared_task
def send_mail_message():
    """
    Отправляет уведомления о привычках, которые нужно выполнить сегодня.

    Получает текущее время и просматривает все привычки для определения, следует ли отправлять уведомление.
    """
    # Получаем текущее время
    current_time = datetime.now().time()
    current_day = datetime.now().day

    # Получаем все привычки, исключая связанные привычки
    habits = Habit.objects.all()

    for habit in habits:
        _check_starting(habit, current_day)
        # Разбиваем текущее время и время уведомления привычки на день, часы и минуты
        current_hour, current_minute = current_time.hour, current_time.minute
        habit_day, habit_hour, habit_minute = _get_mailing_time(habit)
        # Сравниваем часы и минуты
        if habit.is_starting and habit_day == current_day and current_hour == habit_hour \
                and current_minute == habit_minute:
            # Получите сообщение о привычке
            message = habit.get_message()
            # Отправьте уведомление по электронной почте
            subject = "Напоминание о привычке"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [habit.user.email]
            send_mail(subject=subject,
                      message=message,
                      from_email=from_email,
                      recipient_list=recipient_list,
                      fail_silently=False)
            _check_frequency_weekly(habit)
