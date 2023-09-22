from django.shortcuts import render, redirect
from django.views import View
from Tour.models.Package import Package

class Package_page(View):

    def post(self, request):
        package_id = request.POST.get('package')

        # Get the user's wishlist from the session or create an empty dictionary
        wishlist = request.session.get('wishlist', {})

        # Check if the package is already in the wishlist
        if package_id not in wishlist:
            # Package is not in the wishlist, add it to the dictionary
            wishlist[package_id] = None

            # Update the session with the modified wishlist
            request.session['wishlist'] = wishlist

        return redirect('Package_page')

    def get(self, request):
        packages = Package.get_all_Packages()
        return render(request, 'Package_page.html', {'Packages': packages})
