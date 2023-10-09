from django.db import models
from .Country import Country

class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='package_images/')  # Updated path
    duration = models.IntegerField(default=1)
    max_participants = models.PositiveIntegerField(default=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_packages_by_id(ids):
        return Package.objects.filter(id__in=ids)

    @staticmethod
    def get_all_packages():
        return Package.objects.all()

    @staticmethod
    def get_all_packages(search_query=None):
        packages = Package.objects.all()

        if search_query:
            # Filter packages based on the search query
            packages = packages.filter(name__icontains=search_query)

        return packages