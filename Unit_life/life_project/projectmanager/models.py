from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.db.models import Count, F
from django.db.models.functions import Extract

from django.db.models.functions import Length




class Project(models.Model):
    # Defining the fields for the model
    project_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False) 

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
    @classmethod
    def get_project_lengths(cls):
        # Using Django's annotate and F expressions to calculate lengths
        return cls.objects.annotate(length=Length('project_name') + Length('description')).values_list('length', flat=True)

    @classmethod
    def projects_per_month(cls):
        # Using Django's ORM to group and count projects per month and year
        return cls.objects.annotate(
            year=Extract('created_at', 'year'),
            month=Extract('created_at', 'month')
        ).values('year', 'month').annotate(count=Count('id')).order_by('year', 'month')
        
        
    @classmethod
    def recent_projects(cls, limit=5):
        # Simple ORM query to get recent projects
        return cls.objects.order_by('-created_at')[:limit]


def get_default_user():
    # Implement logic to find the default user
    # Example: return User.objects.get(username='defaultuser').id
    return User.objects.filter(is_superuser=True).first().id

def one_week_from_today():
        return timezone.now() + timedelta(weeks=1)
























def add_task(self, task):
    self.tasks.append(task)

def total_tasks(self):
    return len(self.tasks)

def completed_tasks(self):
    return len([task for task in self.tasks if task.status == "Completed"])
        
def get_project_lengths():
            # An example of how to use raw SQL inside a model
        sql = text("SELECT length(name) + length(description) FROM projects")
        return db.session.execute(sql).scalars().all()  # Returns just the integers
        
        
def projects_per_month():
    sql = text("""
        SELECT EXTRACT(YEAR FROM created_at) as year, 
        EXTRACT(MONTH FROM created_at) as month, 
        COUNT(*) 
        FROM projects 
        GROUP BY year, month
        ORDER BY year, month;
        """)
    return db.session.execute(sql).all()

def recent_projects(limit=5):
    return Project.query.order_by(Project.created_at.desc()).limit(limit).all()
















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
