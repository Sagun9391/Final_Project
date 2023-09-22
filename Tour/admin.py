from django.contrib import admin
from .models.Package import Package
from .models.Country import Country
from .models.Customer import Customer
from .models.Bookings import Booking
from .models.Contact_us import Contact_Us


class AdminPackage(admin.ModelAdmin):
    list_display = ['name', 'price', 'Country']


class AdminCountry(admin.ModelAdmin):
    list_display = ['name']


class AdminBookings(admin.ModelAdmin):
    list_display = ['customer', 'email', 'phone_number', 'address']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['full_name']


class AdminContact_us(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']


# Register your models here.
admin.site.register(Package, AdminPackage)
admin.site.register(Country, AdminCountry)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Booking, AdminBookings)
admin.site.register(Contact_Us, AdminContact_us)
