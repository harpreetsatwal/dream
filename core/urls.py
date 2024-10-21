from django.urls import path

from . import views

urlpatterns = [
    # eg: /web/
    path("", views.alltasks, name="alltasks"),
]
