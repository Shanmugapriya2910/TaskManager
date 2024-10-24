from django.urls import path, include

urlpatterns = [
    path('api/', include('tasks.urls')),  # Include the tasks API routes
]




