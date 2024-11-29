from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)   
    start_date = models.DateTimeField("date started")


