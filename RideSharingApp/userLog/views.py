from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth 
from django.urls import reverse
from django.contrib import messages

def rideRequest(request):
    return render(request, "userLog/ride_request.html")

def owner(request):
    return render(request, "userLog/owner_page.html")

def driverInfo(request):
    return render(request, "userLog/driver_info_form.html")

def driverPage(request):
    return render(request, "userLog/driver_page.html")

def riderPage(request):
    return render(request, "userLog/rider_page.html")

def home(request):
    return render(request, "userLog/home.html")

def login(request):
    if request.method == "POST":
        username = request.Post['username']
        password = request.Post['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('userLog:home'))
        else: 
            messages.info(request, 'invalid user ')
            return HttpResponseRedirect(reverse('userLog:login'))
    else:
        messages.info(request, 'MESSAGE')
        return render(request, "userLog/login.html")

def register(request):
    if request.method == 'POST':
        firstName = request.Post['firstName']
        lastName = request.Post['email']
        email = request.Post['email']
        username = request.Post['username']
        password = request.Post['password']

        if(User.objects.filter(username = username).exist()):
            messages.info(request, 'Username already exists')
        elif(User.objects.filter(email = email).exist()):
            messages.info(request, 'email already exists')
        else:
            user = User.objects.create_user(username = username, password = password, email = email, first_name = firstName, last_name = lastName)
            user.save()

        messages.info(request, 'Your account has been updated!')
        return HttpResponseRedirect(reverse('userLog:login'))
    else: 
        messages.info(request, 'hello haha')
        return render(request, "userLog/register.html")