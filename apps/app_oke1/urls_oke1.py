from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('/infor',views.newFunction, name="infor"),
    path('/school',views.School, name="school"),
]
