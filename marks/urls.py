from django.urls import path
from . import views

urlpatterns = [
    path("", views.mark_list, name="mark_list"),
    path("add/", views.add_mark, name="add_mark"),
]