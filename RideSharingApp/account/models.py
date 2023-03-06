from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone



CAR_CHOICES = (
    ('SUV','SUV'),
    ('Sedan', 'Sedan'),
    ('Crossover','Crossover'),
    ('Minivan','Minivan'),

)
CarRequest_CHOICES = (
    ('Any','Any'),
    ('SUV','SUV'),
    ('Sedan', 'Sedan'),
    ('Crossover','Crossover'),
    ('Minivan','Minivan'),
)
CAR_STATUS = { 
    ('OPEN','OPEN'),
    ('COMFIRM', 'COMFIRM'),
    ('COMPLETE','COMPLETE'),
}
# Create your models here.
class DriverInfo(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    carType = models.CharField(max_length=20, choices=CAR_CHOICES, default='SUV')
    max_passenger = models.PositiveBigIntegerField(default = 1)
    license = models.CharField(max_length = 200)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.carType + "_" + self.lname

class RideRequestInfo(models.Model):
    address = models.CharField(max_length = 200)
    dateTime = models.DateTimeField(auto_now_add=False, auto_now=False)
    num_passenger = models.PositiveBigIntegerField(default = 1)
    carType = models.CharField(max_length=20, choices=CarRequest_CHOICES, default='Any')
    isShared = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=CAR_STATUS, default='OPEN')
    specialRequest = models.CharField(max_length = 200, null=True, default='N/A')
    driver = models.CharField(max_length = 200, null=True, default=None)
    spotAvaliableLeft = models.PositiveBigIntegerField(default = 0)
    #owner = models.CharField(max_length = 200, null=True, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    driver_fname = models.CharField(max_length = 200, null=True, default=None)
    driver_lname = models.CharField(max_length = 200, null=True, default=None)
    license = models.CharField(max_length = 200, null=True, default=None)
    user = models.CharField(max_length = 200)
    sharer = models.ManyToManyField(User, related_name='sharer')


    def __str__(self):
        return self.address

class SharerInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    involvedRides = models.ManyToManyField(RideRequestInfo)
