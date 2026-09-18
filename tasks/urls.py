from django.urls import path
from .views import task_list, create_task, close_task, toggle_task, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('close/<int:task_id>/', close_task, name='close_task'),
    path('toggle/<int:task_id>/',toggle_task,name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]