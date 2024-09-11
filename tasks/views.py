from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html')


def tasks(request):
    tasks = Task.objects.order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


def task(request, task_id):
    task = Task.objects.get(id=task_id)
    # Проверка того, что тема принадлежит текущему пользователю.
    # if topic.owner != request.user:
    #     raise Http404
    context = {'task': task}
    return render(request, 'tasks/task.html', context)