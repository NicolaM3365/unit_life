# views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,  Task, TaskComment, TaskAttachment
  # Import the Project model from your app's models.py
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    return render(request, 'home.html', {'projects':Project.objects.all()})


def project_list(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 10)  # Show 10 projects per page

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    
    return render(request, 'projectmanager/home.html', {'projects': projects})

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







def home(request):
    return render(request, 'home.html', {'projects':Project.objects.all()})

class ProjectListView(ListView):
    model = Project
    template_name = 'projectmanager/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-start_date']

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'description', 'start_date', 'end_date', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['project_name', 'description', 'start_date', 'end_date', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.

    def test_func(self):
        post = self.get_object()
        # return self.request.user == post.author
        if self.request.user == post.author:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        # return self.request.user == post.author
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'projectmanager/about.html', {'title': 'About'})
