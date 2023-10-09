from django.shortcuts import render
from django.views import View
from Tour.models import Location

class LocationListView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            # If there is a search query, filter locations based on the query
            locations = Location.objects.filter(name__icontains=query)
        else:
            # If no search query, retrieve all locations
            locations = Location.objects.all()

        return render(request, 'Location.html', {'locations': locations, 'query': query})
