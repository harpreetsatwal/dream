from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Project
from .models import Job

def index(request):
    latest_projects_list = Project.objects.order_by("-start_date")[:5]
    template = loader.get_template("core/index.html")
    context = {
        "latest_projects_list": latest_projects_list,
    }
    return HttpResponse(template.render(context, request))

def projects(request):
    latest_projects_list = Project.objects.order_by("-start_date")[:5]
    template = loader.get_template("core/projects.html")
    context = {
        "latest_projects_list": latest_projects_list,
    }
    return HttpResponse(template.render(context, request))

def jobs(request):
    current_job = Job.objects.filter(done=False,in_use=False).order_by('-created').first()
    template = loader.get_template("core/jobs.html")
    context = {
        "current_job": current_job,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("core/login.html")
    context = {
    }
    return HttpResponse(template.render(context, request))

def error404(request):
    template = loader.get_template("core/error-404.html")
    context = {
    }
    return HttpResponse(template.render(context, request))