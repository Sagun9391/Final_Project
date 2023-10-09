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
    PAYMENT_STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]

    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    email = models.EmailField(max_length=50, default='', blank=True)
    phone_number = models.CharField(max_length=15, default='', blank=True)
    address = models.CharField(max_length=255, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    Package_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Failed')
    payment_reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer.full_name}"
