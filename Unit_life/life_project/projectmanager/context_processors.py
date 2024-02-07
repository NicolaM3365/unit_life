# projectmanager/context_processors.py
from datetime import datetime, timedelta
from .models import Project

def latest_projects(request):
    # Calculate the start date for the past week
    start_date_week_ago = datetime.now() - timedelta(days=7)
    
    # Filter projects started after the calculated start date
    recent_projects = Project.objects.filter(start_date__gte=start_date_week_ago)
    
    return {'latest_projects': recent_projects}