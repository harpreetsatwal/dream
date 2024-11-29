from django.urls import path

from . import views

urlpatterns = [
    # eg: /web/
    path("", views.index, name="index"),
]
