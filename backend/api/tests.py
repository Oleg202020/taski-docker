# backend/api/tests.py
"""Тесты API (pytest-style, но на unittest)."""

from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    """Smoke-тесты эндпоинтов /api/tasks/."""

    def setUp(self):
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности списка задач — должен вернуть 200."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания задачи — создаёт задачу и возвращает 201."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
