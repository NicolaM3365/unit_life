
from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView
)

from . import views

# app_name = 'projectmanager'


# urlpatterns = [
#     # print("Mapping 'projectmanager-home' URL pattern..."),
#     path('', ProjectListView.as_view(), name='projectmanager-home'),
#     path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
#     # path('', views.home, name='projectmanager-home'),
#     path('about/',views.about, name='projectmanager-about'),
#     # path('projects/', views.project_list, name='project-list'),
#     path('project/new/', ProjectCreateView.as_view(), name='project-create'),
#     # path('projects/<int:project_id>/', views.project_detail, name='project-detail'),
#     path('projects/<int:project_id>/tasks/', views.task_list, name='task-list'),
#     path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task-detail'),
#     path('projects/<int:project_id>/tasks/<int:task_id>/comments/', views.comment_list, name='comment-list'),
#     path('projects/<int:project_id>/tasks/<int:task_id>/attachments/', views.attachment_list, name='attachment-list'),
# ]


urlpatterns = [
    path('', ProjectListView.as_view(), name='projectmanager-home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('about/', views.about, name='projectmanager-about'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:project_id>/task/', views.task_list, name='task-list'),
    path('project/<int:project_id>/task/<int:task_id>/', views.task_detail, name='task-detail'),
    path('project/<int:project_id>/task/<int:task_id>/comments/', views.comment_list, name='comment-list'),
    path('project/<int:project_id>/task/<int:task_id>/attachments/', views.attachment_list, name='attachment-list'),
]