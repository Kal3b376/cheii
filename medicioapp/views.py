from django.shortcuts import render, redirect
from medicioapp.models import Contact,Appointment
from medicioapp.forms import AppointmentForm

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

def departments(request):
    return render(request,'departments.html')

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


def appointment(request):
    if request.method == 'POST':
        all= Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']
                        )
        all.save()
        return redirect('/appointment')
    else:
        return render(request, 'appointment.html')

def branches(request):
    if request.method == 'POST':
        all= Contact(name=request.POST['name'],
                 location=request.POST['location'],
                 manager=request.POST['manager'],
                 email=request.POST['email'],
                 )
        all.save()
        return redirect('/branches')
    else:
        return render(request, 'branches.html')

def show(request) :
    information = appointment.objects.all()
    return render(request,'show.html',{'data':information})

def delete(request,id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show.html')

def edit(request,id):
    appointment = Appointment.objects.get(id=id)
    return render(request,'edit.html',{'x':appointment})

def update(request,id):
    if request.method == 'POST':
        appointment = Appointment.objects.get(id=id)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
            return render(request, 'edit.html',)
    else:
        return render(request, 'edit.html',)

def register(request):
    return render(request, 'register.html')
