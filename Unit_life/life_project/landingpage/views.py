from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # Your landing page view logic here
    return render(request, 'landingpage/home.html')

def about(request):
    return render(request, 'landingpage/about.html', {'title': 'About'})

def accordian(request):
    return render(request, 'landingpage/accordian.html', {'title': 'Accordian'})
