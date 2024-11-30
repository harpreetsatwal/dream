from django.db import models
import datetime
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField("Date Started", default=datetime.date.today)
    created = models.DateTimeField("Date Created", default=datetime.date.today)
    last_updated = models.DateTimeField("Date Last Updated", default=datetime.date.today)
    total_jobs = models.IntegerField(default=0,blank=True)
    jobs_done = models.IntegerField(default=0, blank=True)

class Job(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    aim = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    in_use = models.BooleanField(default=False)
    text_before = models.CharField(max_length=500)
    text_after = models.CharField(max_length=500,default="-------")
    created = models.DateTimeField("Date Created")
    updated = models.DateTimeField("Date Updated")
