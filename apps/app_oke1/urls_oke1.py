from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    # note dc k
    path('/infor',views.newFunction, name="infor"),
    # note thoi
    path('/school',views.School, name="school"),
]
