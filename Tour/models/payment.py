# models.py

from django.db import models
from Tour.models.Package import Package
from datetime import datetime

class Payment(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    payment_date = models.DateTimeField(default=datetime.now)  # Provide a default value, adjust as needed

    def __str__(self):
        return f"Payment for {self.package}"
