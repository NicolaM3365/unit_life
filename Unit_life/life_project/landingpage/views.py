from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # Your landing page view logic here
    return render(request, 'landingpage/home.html')

