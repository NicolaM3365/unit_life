from django.shortcuts import render

# Next week, we will start introduce the Django database settings and ORM.
# But for now, we'll just use a list of dictionaries to represent our blog posts.
POSTS = [
    {
        "author": "Steve K",
        "title": "First Blog Post",
        "content": "Content for the first post",
        "date_posted": "16/09/2023",
    },
    {
        "author": "John K",
        "title": "Second Blog Post",
        "content": "Content for the second post",
        "date_posted": "18/09/2023",
    },
    {
        "author": "Jane K",
        "title": "Third Blog Post",
        "content": "Content for the third post",
        "date_posted": "19/09/2023",
    },
    {
        "author": "Batman",
        "title": "Fourth Blog Post",
        "content": "Content for the fourth post",
        "date_posted": "19/09/2023",
    },
]


def home(request):
    context = {"posts": POSTS}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
