"""сериализатор."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """сериализатор."""

    class Meta:
        """мета."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
