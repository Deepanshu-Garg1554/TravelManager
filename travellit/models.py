from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=20)
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    number = models.IntegerField(default=2)

class Detailed_desc(models.Model):
    dest_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=20)
    days = models.IntegerField(default=5)
    price = models.IntegerField(default=20000)
    rating = models.IntegerField(default=5)
    dest_name = models.CharField(max_length=25)
    img1=models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    desc = models.TextField()
    day1= models.CharField(max_length=200)
    day2 = models.CharField(max_length=200)
    day3 = models.CharField(max_length=200)
    day4 = models.CharField(max_length=200)
    day5 = models.CharField(max_length=200)
    day6 = models.CharField(max_length=200)

class hotels(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    room = models.IntegerField()
    price = models.IntegerField()
    city = models.CharField(max_length=20)
    check_in_date = models.DateField(default=datetime.now)
    check_out_date = models.DateField(default=datetime.now)
class flight(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField()
    from_city = models.CharField(max_length=30)  
    to_city = models.CharField(max_length=30)    
    depart = models.DateField(default=datetime.now)
class Booking(models.Model):
    BOOKING_TYPES = (
        ('hotel', 'Hotel'),
        ('package', 'Package'),
        ('flight', 'Flight'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    order_id = models.CharField(max_length=1000, primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.IntegerField()
    paid = models.BooleanField(default=False)
    check_in_date = models.DateField(null=True, blank=True)
    num_passengers = models.IntegerField(null=True, blank=True)
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES,default='hotel')

    def __str__(self):
        return self.order_id