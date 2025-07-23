from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class BusinessGroup(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField(blank=True)

    def clean(self):
        min_lat = float(settings.MAP_BOUNDS_MIN_LAT)
        max_lat = float(settings.MAP_BOUNDS_MAX_LAT)
        min_lng = float(settings.MAP_BOUNDS_MIN_LNG)
        max_lng = float(settings.MAP_BOUNDS_MAX_LNG)

        if not (min_lat <= self.latitude <= max_lat):
            raise ValidationError({'latitude': f'Latitude must be between {min_lat} and {max_lat}.'})
        if not (min_lng <= self.longitude <= max_lng):
            raise ValidationError({'longitude': f'Longitude must be between {min_lng} and {max_lng}.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


class Business(models.Model):
    class Category(models.TextChoices):
        RESTAURANT = 'RESTAURANT', 'Restaurant'
        BAR = 'BAR', 'Bar'
        SHOP = 'SHOP', 'Shop'

    name = models.CharField(max_length=255)
    business_group = models.ForeignKey(BusinessGroup, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
    )
    date_opened = models.DateField()
    date_closed = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Businesses"