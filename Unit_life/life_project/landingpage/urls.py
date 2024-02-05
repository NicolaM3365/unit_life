from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landingpage-home'),  # Define the landing page URL pattern
]

