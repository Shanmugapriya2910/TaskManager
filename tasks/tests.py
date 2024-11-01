
from django.test import TestCase
from _pytest import unittest
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from tasks.models import Task
from tasks.views import create_task

class CreateTaskViewTest(APITestCase):
    @patch('tasks.serializers.TaskSerializer')
    def test_create_task_success(self, MockTaskSerializer):
        # Mock the serializer's behavior
        mock_serializer_instance = MockTaskSerializer.return_value
        mock_serializer_instance.is_valid.return_value = True
        mock_serializer_instance.save.return_value = None  # No need to return anything from save


        task_data = {
            'title': 'New Task',
            'description': 'This is a new task.',
            'completed': False
        }

        response = self.client.post('/api/tasks/create/', task_data, format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], task_data['title'])

        class TaskAPITestCase(APITestCase):
            def setUp(self):
                # Create a sample task for testing
                self.task = Task.objects.create(
                    title='Existing Task',
                    description='This task already exists.',
                    completed=False
                )
                self.task_data = {
                    'title': 'New Task',
                    'description': 'This is a new task.',
                    'completed': False
                }
                self.updated_task_data = {
                    'title': 'Updated Task',
                    'description': 'This task has been updated.',
                    'completed': True
                }

            @patch('tasks.serializers.TaskSerializer')
            def test_create_task_success(self, MockTaskSerializer):

                mock_serializer_instance = MockTaskSerializer.return_value
                mock_serializer_instance.is_valid.return_value = True
                mock_serializer_instance.save.return_value = None

                response = self.client.post('/api/tasks/create/', self.task_data, format='json')

                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(response.data['title'], self.task_data['title'])

            @patch('tasks.serializers.TaskSerializer')
            def test_update_task_success(self, MockTaskSerializer):

                mock_serializer_instance = MockTaskSerializer.return_value
                mock_serializer_instance.is_valid.return_value = True
                mock_serializer_instance.save.return_value = None

                response = self.client.put(f'/api/tasks/update/{self.task.id}/', self.updated_task_data, format='json')

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data['title'], self.updated_task_data['title'])

            def test_get_task_success(self):
                response = self.client.get(f'/api/tasks/{self.task.id}/')

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data['title'], self.task.title)

            def test_get_all_tasks_success(self):
                response = self.client.get('/api/tasks/')

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertTrue(isinstance(response.data, list))
                self.assertGreater(len(response.data), 0)

            def test_delete_task_success(self):
                response = self.client.delete(f'/api/tasks/delete/{self.task.id}/')

                self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
                self.assertEqual(Task.objects.filter(id=self.task.id).count(), 0)

            def test_get_task_not_found(self):
                response = self.client.get('/api/tasks/999/')

                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
                self.assertEqual(response.data['error'], 'Task not found')

            def test_update_task_not_found(self):
                response = self.client.put('/api/tasks/update/999/', self.updated_task_data, format='json')

                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
                self.assertEqual(response.data['error'], 'Task not found')

            def test_delete_task_not_found(self):
                response = self.client.delete('/api/tasks/delete/999/')

                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
                self.assertEqual(response.data['error'], 'Task not found')
