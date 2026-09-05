from django.urls import path
from . import views

urlpatterns = [

    path("", views.university_list, name="university_list"),

    path("add/", views.add_university, name="add_university"),

    path("edit/<int:id>/", views.edit_university, name="edit_university"),

    path("delete/<int:id>/", views.delete_university, name="delete_university"),

]