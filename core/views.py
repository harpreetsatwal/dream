from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def alltasks(request):
    return HttpResponse("Hello, world. You're at the core alltasks view.")
