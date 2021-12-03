from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
<<<<<<< HEAD
    path('/infor',views.newFunction, name="infor"),
]
=======
    path('/student',views.StudentManagement, name="add"),
]
>>>>>>> 9c63b2d (add function StudentManagement)
