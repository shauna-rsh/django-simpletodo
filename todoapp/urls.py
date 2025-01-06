from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Home page with task list
    path('add/', views.add_task, name='add_task'),  # Add task page
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),  # Mark task as complete
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task
]
