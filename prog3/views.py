from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    students = ['yash','john','doe']
    fruits = ['apple','banana','mango']

    return render(request,'prog3/home.html',{'students':students,'fruits':fruits})