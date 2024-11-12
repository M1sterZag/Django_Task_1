from django.urls import path, include
from . import views
app_name = 'tasks'
urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.tasks, name="tasks"),
    path("new_task/", views.new_task, name="new_task"),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/toggle_status/', views.toggle_task_status, name='toggle_task_status'),
]