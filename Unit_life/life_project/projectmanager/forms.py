# forms.py

from django import forms
from .models import Project, Event

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'status', 'managed_project']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date']
