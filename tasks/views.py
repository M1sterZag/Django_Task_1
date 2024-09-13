from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

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


def new_task(request):
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TaskForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:tasks')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = TaskForm(instance=task)
    else:
        # Отправка данных POST; обработать данные.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task', task_id=task.id)
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
    return redirect("tasks:tasks")