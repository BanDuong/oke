from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'name': 'Ban', 'age': 22, 'gender': 'male'}
    return render(request=request,template_name="app_oke1/index.html",context=context)

def newFuntion(request):
    return render(request, "<p>hello</p>")
