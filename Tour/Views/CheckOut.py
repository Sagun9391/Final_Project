from django.shortcuts import render, redirect
from django.views import View
from Tour.models.Package import Package
from Tour.models.Bookings import Booking
from Tour.models.Customer import Customer
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

class Checkout(View):
    def post(self, request):
        package_id = request.POST.get('package_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer')

        if package_id:
            package = Package.objects.get(id=package_id)
            price = package.price

            # Create a Booking object
            booking = Booking(
                package=package,
                customer=Customer.objects.get(id=customer),
                price=price,
                email=email,
                phone_number=phone,
                address=address,
                date=datetime.datetime.today()
            )
            booking.save()

            # Redirect to the payment page
            return HttpResponseRedirect(reverse('Payment'))
        else:
            return redirect('wishlist')
