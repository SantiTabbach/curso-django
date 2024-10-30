from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render


# Create your views here.


def index(req):
    title = "Welcome Baquito app"
    return render(req, "index.html", {"title": title})


def hello(_req, username):
    return HttpResponse(f"<h2>Hola, {username}</h2>")


def projects(req):
    projects = Project.objects.all()
    return render(req, "projects.html", {"projects": projects})


def tasks(req):
    tasks = Task.objects.all()
    return render(req, "tasks.html", {"tasks": tasks})
