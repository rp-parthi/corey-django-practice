from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home page - Blog</h1>")

def contact(request):
    return HttpResponse("<p>Contact me</p>")
