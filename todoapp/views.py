from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task

# View to display all tasks
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'task_list.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the form
        description = request.POST.get('description')  # Get the description
        Task.objects.create(title=title, description=description)  # Create a new task
        return redirect('task_list')  # Redirect to the task list
    return render(request, 'add_task.html')  # Render the add task form

# View to mark a task as completed
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# View to delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')