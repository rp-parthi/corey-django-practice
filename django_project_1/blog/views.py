from django.shortcuts import render

posts = [
    {
        "title": "Blog title 1",
        "content": "Blog content 1",
        "author": "Parthiban",
        "date_posted": "01, May, 2026"
    },
    {
        "title": "Blog title 2",
        "content": "Blog content 2",
        "author": "Parthi",
        "date_posted": "02, May, 2026"   
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')