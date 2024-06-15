from datetime import timedelta

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

from config.settings import NULLABLE


class Habit(models.Model):
    """Модель привычки"""

    PERIODICITY_CHOICES = {
        1: "Каждый день",
        2: "Через день",
        3: "Раз в три дня",
        4: "Раз в четыре дня",
        5: "Раз в пять дней",
        6: "Раз в шесть дней",
        7: "Раз в неделю",
    }

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                              verbose_name="Пользователь")
    place = models.CharField(max_length=200, **NULLABLE, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=200, verbose_name="Действие")
    is_enjoyable = models.BooleanField(default=False, verbose_name="Приятная привычка")
    linked_habit = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE,
                                     verbose_name="Связанная приятная привычка")
    periodicity = models.IntegerField(choices=PERIODICITY_CHOICES, default=1, **NULLABLE, verbose_name="Периодичность")
    treat = models.CharField(max_length=200, **NULLABLE, verbose_name="Вознаграждение")
    duration = models.DurationField(validators=[MaxValueValidator(timedelta(seconds=120))],
                                    verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Публичная")

    def __str__(self):
        return f"Привычка '{self.action}' в {self.time} - {self.periodicity}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
