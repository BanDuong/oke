from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'name': 'Ban', 'age': 22, 'gender': 'male'}
    return render(request=request,template_name="app_oke1/index.html",context=context)

def newFuntion(request):
    return render(request, "<p>hello</p>")

def Mangement(request):
    x = 10
    y = 11
    z = 12
    k = 13
    l = 14
    h = 15
    return render(request, "<h2>Management!!!</h2>")
