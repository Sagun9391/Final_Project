from django.db import models
from .Country import Country


class Package(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='package_images/')  # Updated path
    duration = models.IntegerField(default=1)
    max_participants = models.PositiveIntegerField(default=10)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name


    @staticmethod
    def get_packages_by_id(ids):
        return Package.objects.filter(id__in=ids)

    @staticmethod
    def get_all_Packages():
        return Package.objects.all()
