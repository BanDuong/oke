from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
<<<<<<< HEAD
    context = {'name': 'Ban', 'age': 22, 'gender': 'male'}
    return render(request=request,template_name="app_oke1/index.html",context=context)

def newFuntion(request):
    return render(request, "<p>hello</p>")
=======
    #return HttpResponse("oke nhe")
    return render(request=request,template_name="app_oke1/index.html",context={})

def StudentManagement(request):

    context = {'name': 'Nam', 'age': '22', 'gender': 'male', 'school': 'Haui'}
    return render(request, template_name="<h1>say hihihi</h1>", context=context)
>>>>>>> 9c63b2d (add function StudentManagement)
