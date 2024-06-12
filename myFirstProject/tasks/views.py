# tasks/views.py

from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('index')
    return render(request, 'tasks/add_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
