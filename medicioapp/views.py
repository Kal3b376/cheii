from django.shortcuts import render, redirect
from medicioapp.models import Contact


# Create your views

def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request,'services.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    if request.method == 'POST':
        all= Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                     message=request.POST['message'])
        all.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
