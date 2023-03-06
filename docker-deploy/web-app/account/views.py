from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User, auth 
from django.urls import reverse
from django.contrib import messages
from .models import DriverInfo, RideRequestInfo, SharerInfo
from .forms import DriverForm, RideRequestForm, CustomUserCreationForm
from django.core.mail import send_mail, send_mass_mail



def Join(request, id, numPassenger):
    sharer = request.user
    object = RideRequestInfo.objects.get(id = id)
    object.num_passenger = object.num_passenger + numPassenger
    object.sharer.add(sharer)
    object.save()

    if SharerInfo.objects.filter(user = sharer).exists():
        shareObject = SharerInfo.objects.get(user = sharer).involvedRides.add(object)
    else:
        shareObject = SharerInfo.objects.create(user=sharer)
        shareObject.involvedRides.add(object)
        shareObject.save()
    return redirect('Ridesharer')

def Complete(request, id):
    object = RideRequestInfo.objects.get(id = id)
    object.status = 'COMPLETE'
    object.save()
    return redirect('DriverPage')

def ViewRideDetail(request, id):
    object = RideRequestInfo.objects.get(id = id)
    return render(request, "registration/driver_claim_view.html", {'object': object})

def Comfirm(request, id):
    object = RideRequestInfo.objects.get(id = id)
    object.status = 'COMFIRM'
    object.driver = request.user.username
    user_points = DriverInfo.objects.get(user = request.user)
    object.driver_fname = user_points.fname
    object.driver_lname = user_points.lname
    object.license = user_points.license
    object.spotAvaliableLeft = user_points.max_passenger - object.num_passenger
    object.save()
    
    send_mail(
        'Ride Service Status Update',
        'Your requested ride has been comfirmed',
        'dukesh694@outlook.com',
        [object.owner.email],
        fail_silently=False,
    )
    recipient_list = [sharer.email for sharer in object.sharer.all()]
    message = (
        'Ride Service Status Update', 
        'Your requested ride has been comfirmed', 
        'dukesh694@outlook.com', 
        recipient_list
    )
    send_mass_mail((message,))
    return redirect('DriverPage')

def SharerRideSearch(request):
    if request.method == "POST":
        destination = request.POST['address']
        earlyTime = request.POST['dateTimeEarly']
        lateTime = request.POST['dateTimeLate']
        numPassenger = request.POST['num_passenger']
        objects = RideRequestInfo.objects.filter(isShared = True, status = 'OPEN')
        objects = objects.filter(address = destination, 
                                 dateTime__gte = earlyTime, 
                                 dateTime__lte = lateTime,
                                )
        return render(request, "registration/sharer_search.html", {'objects':objects, 'numPassenger':numPassenger})
    else:
        return render(request, "registration/rideshare_page.html")    

def DriverRideSearch(request):
    if request.method == "POST":
        carType = request.POST['carType']
        max_cap = request.POST['num_passenger']
        specialR = request.POST['specialRequest']
        objects = RideRequestInfo.objects.filter(
            status = 'OPEN', 
            num_passenger__lte = max_cap, 
            carType__in = ['Any', carType]
        )
        if specialR is not None:
           objects = objects.filter(specialRequest = specialR)
        if max_cap is None:
            return render(request, "registration/driver_page.html")
        return render(request, "registration/driver_search.html", {'objects':objects})
    else:
        return render(request, "registration/driver_page.html")

def RideRequest(request):
    if request.method == "POST":
        form = RideRequestForm(request.POST or None)
        print("here1")
        if form.is_valid():
            print("here2")
            share=(request.POST['isShared']=="True")
            RideRequest = RideRequestInfo.objects.create(
                address = request.POST['address'], 
                dateTime = request.POST['dateTime'],
                carType = request.POST['carType'],
                num_passenger = request.POST['num_passenger'],
                specialRequest = request.POST['specialRequest'],
                isShared=share,
                owner = request.user,
                user = str(request.user.id),
            )
            #print(RideRequest.dateTime)
            return render(request, "registration/owner_page.html")
        else:
            print("here3")
            return render(request, "registration/ride_request.html")
    else:   
        print("here4") 
        return render(request, "registration/ride_request.html")    

def RequestEdit(request,id):
    if request.method == "POST":
        form = RideRequestForm(request.POST or None)
        if form.is_valid():
            user = request.user
            defaults= {
                'address' : request.POST['address'],
                'dateTime' : request.POST['dateTime'],
                'carType' : request.POST['carType'],
                'num_passenger' : request.POST['num_passenger'],
                'isShared' : request.POST['isShared'],
                'specialRequest' : form.cleaned_data['specialRequest']
            }
            share=request.POST['isShared'], 
            share=(share=="True")
            ownerR = RideRequestInfo.objects.update_or_create(id = id, defaults=defaults)[0]
            return redirect('home')
        else:
            return render(request, "registration/request_edit.html",{'id':id})
    else:    
        return render(request, "registration/request_edit.html",{'id':id})


def DriverDB(request):
    all_driver = DriverInfo.objects.all
    return render(request,"registration/DriverDB.html", {'all' : all_driver})
    
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def DriverRegister(request):
    if request.method == "POST":
        form = DriverForm(request.POST or None)
        if form.is_valid():
            #form.save()
            user = request.user
            defaults= {'fname' : request.POST['fname'],
                'lname' : request.POST['lname'],
                'carType' : request.POST['carType'],
                'license' : request.POST['license'],
                'max_passenger' : request.POST['max_passenger'],
            }
            driver = DriverInfo.objects.update_or_create(user = user, defaults=defaults)[0]
            
            #driver = DriverInfo.objects.filter(user = user)
            return render(request, "registration/driver_page.html",{'driver':driver})
        else:
            return render(request, "registration/driver_info.html",{})
    else:
        form = DriverForm()
        return render(request, "registration/driver_info.html",{})

def ShareStatusView(request):
    sharer = request.user
    if SharerInfo.objects.filter(user = sharer).exists():
        shareRides = SharerInfo.objects.get(user = sharer).involvedRides.all()
        return render(request,"registration/Share_StatusView.html", {'shareRides' : shareRides})
    else:
        return render(request,"registration/Share_StatusView.html", {})

def Owner_StatusView(request):
    user = request.user
    if RideRequestInfo.objects.filter(owner = user).exists():
        owner_status = RideRequestInfo.objects.filter(owner = user)
        return render(request, "registration/Owner_StatusView.html",{'all': owner_status})
    else:
        return render(request, "registration/Owner_StatusView.html",{})
    # status = RideRequestInfo.objects.filter(owner=user)
    # if RideRequestInfo.objects.filter(sharer=shared).exists():
    #     status = RideRequestInfo.objects.filter(sharer=shared)
    
    #     print('here1')
    #     return render(request,"registration/StatusView_Owner.html", {'all' : status})
    # if RideRequestInfo.objects.filter(owner=user).exists():
    #     status = RideRequestInfo.objects.filter(owner=user)
    #     print('here2')
      
    #     return render(request,"registration/StatusView_Owner.html", {'all' : status})
    # else:
    #     print('here3')
    #     return render(request,"registration/StatusView_Owner.html", {'all' : status})

def DriverPage(request):
    user = request.user
    if DriverInfo.objects.filter(user=user).exists():
        driver = DriverInfo.objects.filter(user = user)[0]
        requests = RideRequestInfo.objects.filter(driver = request.user.username).filter(status = 'COMFIRM')
        return render(request, "registration/driver_page.html",{'driver':driver,'requests':requests})
    else:
        return redirect('DriverRegister')

def Owner(request):
    return render(request, "registration/owner_page.html")

def Ridesharer(request):
    return render(request, "registration/rideshare_page.html")
