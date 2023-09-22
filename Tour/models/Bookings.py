# models.py
from django.db import models
from .Package import Package
from .Customer import Customer
import datetime

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
    ]

    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    email = models.EmailField(max_length=50, default='', blank=True)
    phone_number = models.CharField(max_length=15, default='', blank=True)
    address = models.CharField(max_length=255, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
