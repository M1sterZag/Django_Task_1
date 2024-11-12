from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.http import JsonResponse
from django.http import Http404

# Главная страница
def index(request):
    return render(request, 'tasks/index.html')

# Страница всех задач
@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)

# Страница создания новой задачи
@login_required
def new_task(request):
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('tasks:tasks')
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)

# Страница редактирования задачи
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:tasks')  # Перенаправление на страницу всех задач
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)

# Страница удаления задачи
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    task.delete()
    return redirect('tasks:tasks')

# Обработчик изменения статуса задачи (выполнена/не выполнена)
@login_required
def toggle_task_status(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method == 'POST':
        task.is_done = not task.is_done
        task.save()
        return JsonResponse({'status': 'success', 'is_done': task.is_done})
    return JsonResponse({'status': 'error'}, status=400)
