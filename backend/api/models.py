"""Модели приложения API."""

from django.db import models


class Task(models.Model):
    """Модель для фиксации задачи и статуса."""

    title = models.CharField('Заголовок', max_length=120)
    description = models.TextField('Описание')
    completed = models.BooleanField('Выполнена', default=False)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def _str_(self) -> str:
        return self.title
