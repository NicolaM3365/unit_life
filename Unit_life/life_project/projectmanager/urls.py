from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    about,
)

from . import views
from .views import calendar_view

urlpatterns = [
    path('', ProjectListView.as_view(), name='projectmanager-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    
    path('about/', about, name='projectmanager-about'),
    path('projects/', views.project_list, name='project-list'),


    path('calendar/', calendar_view, name='calendar'),
    path('statistics/', views.stats, name='statistics'),
    

      # Task URLs
    path('project/<int:project_id>/tasks/', TaskListView.as_view(), name='task-list'),
    path('project/<int:project_id>/task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('project/<int:project_id>/task/new/', TaskCreateView.as_view(), name='task-create'),
    path('project/<int:project_id>/task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    # path('project/<int:project_id>/task/<int:pk>/confirm-delete/', TaskDeleteView.as_view(), name='task-confirm-delete'),
    path('project/<int:project_id>/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
