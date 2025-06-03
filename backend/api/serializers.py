"""Сериализаторы DRF."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор модели Task для всех CRUD-операций."""

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')
