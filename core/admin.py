from django.contrib import admin

# Register your models here.
from .models import Project
from .models import Job
admin.site.register(Project)
admin.site.register(Job)
