from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse



class Project(models.Model):
    # Defining the fields for the model
    project_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    
    # Using two separate fields for start and end dates
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    managed_project = models.ForeignKey(User, related_name='managed_projects', on_delete=models.CASCADE)
    # Assuming stakeholders are represented as a string of names
    # In a more complex implementation, this might be a many-to-many field linking to a User or another model
    stakeholders = models.CharField(max_length=500, null=True, blank=True)

    # Status could be a choice field if you have specific statuses that a project can have
    STATUS_CHOICES = [
        ('PL', 'Planning'),
        ('OG', 'Ongoing'),
        ('CP', 'Completed'),
        ('HL', 'On Hold'),
        ('CN', 'Cancelled'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PL')

    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self): # Change here
        return reverse('project-detail', kwargs={'pk': self.pk}) # Change here to bring the user to the post detail view

def get_default_user():
    # Implement logic to find the default user
    # Example: return User.objects.get(username='defaultuser').id
    return User.objects.filter(is_superuser=True).first().id

def one_week_from_today():
        return timezone.now() + timedelta(weeks=1)

class Task(models.Model):
    # Defining the fields for the model
    task_name = models.CharField(max_length=200, default='New Task')
    description = models.TextField()
    
    # Linking each task to a specific project
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    
    # Assigning the task to a user. This assumes that a task is managed by a single user.
    # For multiple users, consider using a ManyToManyField.
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE, default=get_default_user)
    
    # Due date for the task
    due_date = models.DateField(default=one_week_from_today)
    
    
    
    # Task priority could be a choice field to have specific priorities
    PRIORITY_CHOICES = [
        ('HI', 'High'),
        ('MD', 'Medium'),
        ('LO', 'Low'),
    ]
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='MD')
    
    # Task status, similar to the Project status
    STATUS_CHOICES = [
        ('NT', 'Not Started'),
        ('IP', 'In Progress'),
        ('CO', 'Completed'),
        ('BL', 'Blocked'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NT')

    def __str__(self):
        return self.task_name
    
class TaskComment(models.Model):
    # Defining the fields for the model
    comment = models.TextField()    
    # Linking each comment to a specific task
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    # Linking each comment to a specific user

    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    # Timestamp for the comment
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
    
class TaskAttachment(models.Model):

    # Defining the fields for the model
    attachment = models.FileField(upload_to='task_attachments/')
    # Linking each attachment to a specific task

    task = models.ForeignKey(Task, related_name='attachments', on_delete=models.CASCADE)
    # Linking each attachment to a specific user

    user = models.ForeignKey(User, related_name='attachments', on_delete=models.CASCADE)

    def __str__(self):

        return self.attachment.name





# models.py


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
