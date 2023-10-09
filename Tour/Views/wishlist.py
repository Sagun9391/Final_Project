# views.py (Wishlist view)
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from Tour.models.Package import Package
from Tour.models.Bookings import Booking
from Tour.Algorithm.recommendation_model import get_package_recommendations


class Wishlist(View):
    def get(self, request):
        # Retrieve the list of package IDs from the user's wishlist
        wishlist_dict = request.session.get('wishlist', {})
        ids = list(wishlist_dict.keys())

        # Fetch the corresponding packages
        packages = Package.get_packages_by_id(ids)

        # Fetch the list of booking IDs associated with the logged-in customer
        customer_id = request.session.get('customer')
        bookings = Booking.objects.filter(customer_id=customer_id).values_list('package_id', flat=True)

        return render(request, 'wishlist.html', {'packages': packages, 'bookings': bookings})


class Detail(View):
    # views.py (Detail view)
    def get(self, request, package_id):
        # Retrieve the package based on the package_id
        package = get_object_or_404(Package, id=package_id)

        # Retrieve the specific attributes you need for the recommendation system
        package_name = package.name  # Package_name
        country = package.country.name  # Country
        price = package.price  # Price
        description = package.description  # Description

        # Now, you can pass these attributes as input to your recommendation system
        recommendations = get_package_recommendations(package_name, country, price, description)

        # Fetch the details of the recommended packages
        recommended_packages = Package.objects.filter(name__in=recommendations)

        # Render a template (e.g., 'Details.html') to display the package details and recommendations
        return render(request, 'Details.html', {'package': package, 'recommended_packages': recommended_packages})
