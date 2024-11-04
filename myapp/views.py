from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
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


def project_detail(req, id):

    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(
        req, "projects/detail.html", {"project": project, "tasks": tasks}
    )


def tasks(req):
    tasks = Task.objects.all()
    return render(req, "tasks/tasks.html", {"tasks": tasks})


def create_task(req):
    if req.method == "GET":
        return render(req, "tasks/create_task.html", {"form": CreateNewTask})
    else:
        Task.objects.create(
            title=req.POST["title"],
            description=req.POST["description"],
            project_id=req.POST["project"],
        )
        return redirect("tasks")


def create_project(req):
    if req.method == "GET":
        return render(
            req, "projects/create_project.html", {"form": CreateNewProject}
        )
    else:
        Project.objects.create(
            name=req.POST["name"],
        )
        return redirect("projects")
