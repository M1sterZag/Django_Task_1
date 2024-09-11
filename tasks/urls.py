from django.urls import path, include
from . import views
app_name = 'tasks'
urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/<int:task_id>/", views.task, name="task")
]