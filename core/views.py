from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Project


def index(request):
    latest_projects_list = Project.objects.order_by("-start_date")[:5]
    template = loader.get_template("core/index.html")
    context = {
        "latest_projects_list": latest_projects_list,
    }
    return HttpResponse(template.render(context, request))