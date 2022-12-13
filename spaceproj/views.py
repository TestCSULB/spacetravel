from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from .models import *
from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.

# @login_required(login_url='login')

def index(request):
    return render(request,'spaceproj/index.html')

def plan(request):
    return render(request,'spaceproj/plan.html')

def about(request):
    return render(request,'spaceproj/about.html')

def booking(request):
    return render(request,'spaceproj/booking.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Username or Password')
    return render(request,'spaceproj/login.html')

def register(request):
    form=forms.createUserForm()

    if request.user.is_authenticated:
        return redirect('index')

    if request.method=="POST":
        form=forms.createUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect('login')

        messages.error(request, "Unsuccessful registration. Invalid information.")

    context={'form':form}
    return render(request,'spaceproj/register.html',context)


@login_required(login_url='login')
def contact(request):
    form=forms.ContactForm()

    if request.method=="POST":
        form=forms.ContactForm(request.POST)
        # currentuser=request.user
        #print(form)
        #print(form.is_valid())
        if form.is_valid():
            # form.cleaned_data['UserName']=currentuser.username
            form.save()

            messages.success(request,"Info has been successfully stored")
            return render(request,'spaceproj/contact.html')

        messages.error(request,"Error saving Info")
    context={'form':form}
    return render(request,'spaceproj/contact.html',context)

@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        flight = BookFlight.objects.create(
            UserName=request.user.username,
            TotalSeats=request.POST.get("i1", ""),
            TotalPrice=request.POST.get("i3", ""),
        )

        spliting = str(request.POST.get("i2")).split(',')
        for i in spliting:
            seatName = Seats.objects.create(
                Flight=flight,
                SeatName=i,
            )
        messages.success(request,"Flight has been booked succesfully!!!")

    flightData = Seats.objects.all()
    A1,A2,A3,A4,B1,B2,B3,B4,check = False,False,False,False,False,False,False,False,False

    for i in flightData:
        if i.SeatName == 'A1':
            A1 = True
        elif i.SeatName == 'A2':
            A2 = True
        elif i.SeatName == 'A3':
            A3 = True
        elif i.SeatName == 'A4':
            A4 = True
        elif i.SeatName == 'B1':
            B1 = True
        elif i.SeatName == 'B2':
            B2 = True
        elif i.SeatName == 'B3':
            B3 = True
        elif i.SeatName == 'B4':
            B4 = True

    try:
        userFlight = BookFlight.objects.get(UserName = request.user.username)
        seats = Seats.objects.filter(Flight=userFlight)
        check = True

    except:
        userFlight = []
        seats = []
        check = False


    context={'flight':userFlight,'seats':seats,'check':check,'A1':A1,'A2':A2,'A3':A3,'A4':A4,'B1':B1,'B2':B2,'B3':B3,'B4':B4}
    return render(request,'spaceproj/booking.html',context)
   