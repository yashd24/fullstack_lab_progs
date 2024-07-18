from django.shortcuts import render

def homepage(request):
    return render(request,'prog4/home.html')

def about(request):
    return render(request,'prog4/about.html')

def contact(request):
    return render(request,'prog4/contact.html')