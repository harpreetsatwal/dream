from django.urls import path

from . import views

urlpatterns = [
    # eg: /web/
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("jobs/", views.jobs, name="jobs"),
    path("login/", views.login, name="login"),
]
