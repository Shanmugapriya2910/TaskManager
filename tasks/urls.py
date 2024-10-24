from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),                # Get all tasks
    path('tasks/<int:task_id>/', views.get_tasks, name='get_task'),    # Get task by ID
    path('tasks/create/', views.create_task, name='create_task'),      # Create a new task
    path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),  # Update task
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task
]
