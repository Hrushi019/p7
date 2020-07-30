from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome , from App</h1>")

def home(request):
    return render(request,"app01/home.html",{'name':"Hrushi"})

def fact(request,n):
    n = int(n)
    return HttpResponse("Factorial of {} is {}".format(n,factorial(n)))

def child(request):
    return render(request,"child02.html")

def sam(request):
    return render(request,"app01/sam.html")
