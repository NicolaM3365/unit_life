# views.py

from django.shortcuts import render
from .models import Project  # Import the Project model from your app's models.py

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projectmanager/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'projectmanager/project_detail.html', {'project': project})  
# Path: Unit_life/life_project/projectmanager/views.py


def task_list(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = project.tasks.all()
    return render(request, 'projectmanager/task_list.html', {'project': project, 'tasks': tasks})

def task_detail(request, project_id, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'projectmanager/task_detail.html', {'task': task})

def comment_list(request, project_id, task_id):
    task = Task.objects.get(id=task_id)
    comments = task.comments.all()
    return render(request, 'projectmanager/comment_list.html', {'task': task, 'comments': comments})    
def attachment_list(request, project_id, task_id):
    task = Task.objects.get(id=task_id)
    attachments = task.attachments.all()
    return render(request, 'projectmanager/attachment_list.html', {'task': task, 'attachments': attachments})   