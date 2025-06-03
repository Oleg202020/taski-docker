"""Конфигурация административного интерфейса Django."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Отображение и базовая настройка модели Task в /admin/."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
