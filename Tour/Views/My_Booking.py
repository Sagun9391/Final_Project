# my_booking view
from Tour.models.Bookings import Booking
from django.shortcuts import render


def my_booking(request):
    # Retrieve active booking information for the logged-in customer
    customer_id = request.session.get('customer')

    # Filter bookings based on payment_status and package_status
    bookings = Booking.objects.filter(
        customer_id=customer_id,
        payment_status='Success',
        Package_status='Active'
    )

    return render(request, 'my_booking.html', {'bookings': bookings})
