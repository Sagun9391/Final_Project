# Booking.py (views)
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from Tour.models.Package import Package
from Tour.models.Bookings import Booking
from Tour.models.Customer import Customer
import datetime

class BookingView(View):
    def post(self, request, package_id):
        # Retrieve the package based on the package_id
        package = get_object_or_404(Package, id=package_id)

        # You may need additional logic here to fetch user information
        customer_id = request.session.get('customer')
        customer = get_object_or_404(Customer, id=customer_id)

        # Perform any additional checks or calculations you need for the booking

        # Create a new booking record
        booking = Booking.objects.create(
            package=package,
            customer=customer,
            price=package.price,
            email=customer.email,
            phone_number=customer.phone_number,
            address=customer.address,
            date=datetime.datetime.today(),
            Package_status='Active',
            payment_status='Failed',
        )
        return redirect('Payment', package_id=package_id)
