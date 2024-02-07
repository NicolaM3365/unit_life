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
    

      # Task URLs
    path('project/<int:id>/tasks/', TaskListView.as_view(), name='task-list'),
    path('project/<int:id>/task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('project/<int:id>/task/new/', TaskCreateView.as_view(), name='task-create'),
    path('project/<int:id>/task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('project/<int:id>/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]

# from django.urls import path

# from .views import (
#     ProjectListView,
#     ProjectDetailView,
#     ProjectCreateView,
#     ProjectUpdateView,
#     ProjectDeleteView
# )

# from . import views

# # app_name = 'projectmanager'


# # urlpatterns = [
# #     # print("Mapping 'projectmanager-home' URL pattern..."),
# #     path('', ProjectListView.as_view(), name='projectmanager-home'),
# #     path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
# #     # path('', views.home, name='projectmanager-home'),
# #     path('about/',views.about, name='projectmanager-about'),
# #     # path('projects/', views.project_list, name='project-list'),
# #     path('project/new/', ProjectCreateView.as_view(), name='project-create'),
# #     # path('projects/<int:project_id>/', views.project_detail, name='project-detail'),
# #     path('projects/<int:project_id>/tasks/', views.task_list, name='task-list'),
# #     path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task-detail'),
# #     path('projects/<int:project_id>/tasks/<int:task_id>/comments/', views.comment_list, name='comment-list'),
# #     path('projects/<int:project_id>/tasks/<int:task_id>/attachments/', views.attachment_list, name='attachment-list'),
# # ]


# urlpatterns = [
#     path('', ProjectListView.as_view(), name='projectmanager-home'),
#     path('projects/', views.project_list, name='project-list'),
#     path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
#     path('project/new/', ProjectCreateView.as_view(), name='project-create'),
#     path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
#     path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
#     path('about/', views.about, name='projectmanager-about'),
#     # path('project/<int:project_id>/task/', views.task_list, name='task-list'),
#     # path('project/<int:project_id>/task/<int:task_id>/', views.task_detail, name='task-detail'),
#     # path('project/<int:project_id>/task/<int:task_id>/comments/', views.comment_list, name='comment-list'),
#     # path('project/<int:project_id>/task/<int:task_id>/attachments/', views.attachment_list, name='attachment-list'),
# ]