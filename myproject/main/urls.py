from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="Start"),
path("<int:id>", views.index, name="index")
#path("v1/", views.v1, name="View 1"),
]
