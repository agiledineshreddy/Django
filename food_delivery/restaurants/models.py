from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    price_range = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)  # e.g., Dine-in, Delivery, Pickup
    cuisine = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.cuisine})"
