# my_booking view
from Tour.models.Bookings import Booking
from django.shortcuts import render
def my_booking(request):
    # Retrieve active booking information for the logged-in customer
    customer_id = request.session.get('customer')
    bookings = Booking.objects.filter(customer_id=customer_id, status='Active')

    return render(request, 'my_booking.html', {'bookings': bookings})
