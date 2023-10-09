from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from Tour.models.Package import Package

class Package_page(View):
    def get(self, request):
        # Get the search query from the request
        search_query = request.GET.get('search', '')

        # Get all packages
        all_packages = Package.get_all_packages(search_query)

        # Set the number of packages to display per page
        packages_per_page = 12

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page', 1)

        # Create a Paginator instance and get the current page
        paginator = Paginator(all_packages, packages_per_page)
        current_page = paginator.get_page(page_number)

        return render(request, 'Package_page.html', {'Packages': current_page, 'search_query': search_query})

    def post(self, request):
        # Check if the form is submitted for adding to the wishlist
        if 'package' in request.POST:
            # Get the package ID from the submitted form
            package = request.POST.get('package')

            # Retrieve the user's wishlist from the session or create an empty dictionary
            wishlist = request.session.get('wishlist', {})

            # Check if the package is already in the wishlist
            if package not in wishlist:
                # Package is not in the wishlist, add it to the dictionary
                wishlist[package] = 1  # You can use any value; here, I'm using 1

                # Update the session with the modified wishlist
                request.session['wishlist'] = wishlist

                # Print the updated wishlist to the console for debugging
                print(request.session['wishlist'])

        # Redirect the user back to the 'Package_page'
        return redirect('Package_page')
