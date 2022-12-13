from django.db import models

# Create your models here.

class ContactModel(models.Model):
    # UserName=models.CharField(max_length=50,blank=True)
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    PhoneNumber=models.IntegerField()
    Address1=models.CharField(max_length=200)
    Address2=models.CharField(max_length=200,blank=True)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Zip=models.IntegerField()
    Country=models.CharField(max_length=50)
    DOB=models.DateField()
    InfoAboutUser=models.TextField(max_length=500)
    AdventuresInfo=models.TextField(max_length=500)

class BookFlight(models.Model):
    UserName=models.CharField(max_length=50,blank=True)
    TotalSeats=models.CharField(max_length=200)
    TotalPrice=models.IntegerField()

class Seats(models.Model):
    Flight=models.ForeignKey(BookFlight,on_delete=models.CASCADE)
    SeatName=models.CharField(max_length=50,blank=True)
