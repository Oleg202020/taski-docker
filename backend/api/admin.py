"""админ."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """админ."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
