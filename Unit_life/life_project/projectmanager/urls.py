
from django.urls import path
from . import views

app_name = 'projectmanager'


urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/comments/', views.comment_list, name='comment_list'),
    path('projects/<int:project_id>/tasks/<int:task_id>/attachments/', views.attachment_list, name='attachment_list'),
]
