from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject


# Create your views here.


def index(req):
    title = "Welcome Baquito app"
    return render(req, "index.html", {"title": title})


def hello(_req, username):
    return HttpResponse(f"<h2>Hola, {username}</h2>")


def projects(req):
    projects = Project.objects.all()
    return render(req, "projects/projects.html", {"projects": projects})


def tasks(req):
    tasks = Task.objects.all()
    return render(req, "projects/tasks.html", {"tasks": tasks})


def create_task(req):
    if req.method == "GET":
        return render(req, "tasks/create_task.html", {"form": CreateNewTask})
    else:
        Task.objects.create(
            title=req.POST["title"],
            description=req.POST["description"],
            project_id=1,
        )
        return redirect("/tasks")


def create_project(req):
    if req.method == "GET":
        return render(
            req, "projects/create_project.html", {"form": CreateNewProject}
        )
    else:
        Project.objects.create(
            name=req.POST["name"],
        )
        return redirect("/projects")
