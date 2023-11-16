from django.http import HttpResponse

def home(request):
    return HttpResponse(b'<h1>Blog Home</h1>')


def about(request):
    return HttpResponse(b'<h1>Blog About</h1>')
