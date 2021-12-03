from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('/infor',views.newFuntion, name="infor"),
    path('/student',views.Student, name="students"),
]
