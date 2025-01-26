from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import Task
import pickle
import os

# Load the model and vectorizer
model_path = os.path.join(settings.BASE_DIR, "todoapp", "ml_models", "task_model.pkl")
with open(model_path, "rb") as f:
    vectorizer, model = pickle.load(f)

# View to display all tasks
def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'task_list.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")# Get the title and description from the form
        description = request.POST.get("description")
        task_priority = model.predict(vectorizer.transform([description]))[0]# Predict the priority of the task based on the description
        Task.objects.create(title=title, description=description, priority=task_priority)# Create and save the task with the predicted priority
        return redirect("task_list")# Redirect to the task list page

        # Render the add task form
    return render(request, "add_task.html")


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