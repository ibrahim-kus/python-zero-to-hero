from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#http://127.0.0.1:8000/

# def index(request):
#     return HttpResponse('<h1>Hello From Pagesssss App</h1>')


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

