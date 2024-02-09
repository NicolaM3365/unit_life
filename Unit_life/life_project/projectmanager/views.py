# views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
import statistics

from .models import Project,  Task, TaskComment, TaskAttachment, Event
from .forms import ProjectForm, EventForm
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
    return render(request, 'projectmanager/home.html', {'projects':Project.objects.all()})


def project_list(request):
    projects = Project.objects.all()
    paginator = Paginator(projects,3)  # Show 10 projects per page

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    
    return render(request, 'projectmanager/project_list.html', {'projects': projects})

# def project_detail(request, project_id):
#     project = Project.objects.get(id=project_id)
#     return render(request, 'projectmanager/project_detail.html', {'project': project})  
# # Path: Unit_life/life_project/projectmanager/views.py


# def task_list(request, project_id):
#     project = Project.objects.get(id=project_id)
#     tasks = project.tasks.all()
#     return render(request, 'projectmanager/task_list.html', {'project': project, 'tasks': tasks})

# def task_detail(request, project_id, task_id):
#     task = Task.objects.get(id=task_id)
#     return render(request, 'projectmanager/task_detail.html', {'task': task})

# def comment_list(request, project_id, task_id):
#     task = Task.objects.get(id=task_id)
#     comments = task.comments.all()
#     return render(request, 'projectmanager/comment_list.html', {'task': task, 'comments': comments})    
# def attachment_list(request, project_id, task_id):
#     task = Task.objects.get(id=task_id)
#     attachments = task.attachments.all()
#     return render(request, 'projectmanager/attachment_list.html', {'task': task, 'attachments': attachments})   







def home(request):
    print("Home view accessed...")
    return render(request, 'projectmanager/home.html', {'projects':Project.objects.all()})

class ProjectListView(ListView):
    model = Project
    template_name = 'projectmanager/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-start_date']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(project_name__icontains=q)
        return queryset
    
def calendar_view(request):
    events = Event.objects.all()
    form = EventForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('calendar')
    return render(request, 'projectmanager/calendar.html', {'events': events, 'form': form})
    
    

class ProjectDetailView(DetailView):
    model = Project
    # template_name = 'projectmanager/project_detail.html'  # Specify your template
    # context_object_name = 'project'
    
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name', 'description', 'start_date', 'end_date', 'status', 'managed_project']

    def form_valid(self, form):
        form.instance.managed_project = self.request.user # Set the author on the form
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
        if self.request.user == post.managed_project:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = "project-list"

    def test_func(self):
        post = self.get_object()
        # return self.request.user == post.author
        if self.request.user == post.managed_project:
            return True
        return False

def about(request):
    return render(request, 'projectmanager/about.html', {'title': 'About'})




class TaskListView(ListView):
    model = Task
    template_name = 'projectmanager/task_list.html'  # Specify your template
    context_object_name = 'tasks'
    paginate_by = 10  # Adjust the number of tasks per page

    def get_queryset(self):
        # Assuming each task is related to a project
        return Task.objects.filter(project_id=self.kwargs['project_id']).order_by('due_date')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'projectmanager/task_detail.html'  # Specify your template

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name', 'description', 'status', 'due_date']  # Adjust fields as necessary

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['project_id']  # Assuming a ForeignKey to Project
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['task_name', 'description', 'status', 'due_date']  # Adjust fields as necessary

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['project_id']
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        # Implement your logic to check if the user has permission to update the task
        # Example: return self.request.user == task.assigned_user
        return True

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'projectmanager/task_confirm_delete.html'
    def get_success_url(self):
        # Assuming the task model has a ForeignKey to Project as `project`
        return reverse('project-detail', kwargs={'pk': self.object.project.pk})
    


        # Example: return reverse('project-detail', kwargs={'pk': self.object.project.pk}) 
    # success_url = "project/<int:pk>"  # Redirect to a suitable URL after deletion

    def test_func(self):
        task = self.get_object()
        # Implement your logic to check if the user has permission to delete the task
        # Example: return self.request.user == task.assigned_user
        return True





def stats(request):
    project_lengths = Project.get_project_lengths()
    projects_per_month = Project.projects_per_month()
    recent_projects = Project.recent_projects()
    

    for project in recent_projects:
        project.formatted_created_at = project.created_at.strftime('%Y-%m-%d')
    


    if project_lengths:
        # Using the statistics library to calculate mean and median
        # Ensure you have imported the statistics module
        average_length = round(statistics.mean(project_lengths), 2) if project_lengths else 0
        median_length = round(statistics.median(project_lengths), 2) if project_lengths else 0
        max_length = round(max(project_lengths), 2) if project_lengths else 0
        min_length = round(min(project_lengths), 2) if project_lengths else 0
        total_length = round(sum(project_lengths), 2) if project_lengths else 0

        context = {
            'projects_exist': True,
            'average_length': average_length,
            'median_length': median_length,
            'max_length': max_length,
            'min_length': min_length,
            'total_length': total_length,
            'projects_per_month': projects_per_month,
            'recent_projects': recent_projects
        }
    else:
        context = {
            'projects_exist': False,
            'projects_per_month': projects_per_month,
            'recent_projects': recent_projects
        }

    return render(request, "projectmanager/statistics.html", context)
