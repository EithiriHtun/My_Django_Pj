from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!.And Testing git!")

def index(request):
    my_page = {'insert_me' : "Hello!. Testing by viwe for template!"}
    return render(request,"index.html",context=my_page)
