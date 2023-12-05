from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# posts = [
#     {
#         'author': 'Steve K',
#         'title': 'First Blog Post',
#         'content': 'Content for the first post.',
#         'date_posted': '12/07/2023'
#     },

#      {
#         'author': 'Scott K',
#         'title': 'Second Blog Post',
#         'content': 'Content for the second post.',
#         'date_posted': '13/07/2023'
#     }

# ]

# def home(request):
#     return render(request, 'home.html')

# Create your views here.x
def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
