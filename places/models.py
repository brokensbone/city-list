from django.db import models

class BusinessGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Business(models.Model):
    class Category(models.TextChoices):
        RESTAURANT = 'RESTAURANT', 'Restaurant'
        BAR = 'BAR', 'Bar'
        SHOP = 'SHOP', 'Shop'

    name = models.CharField(max_length=255)
    business_group = models.ForeignKey(BusinessGroup, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=10,
        choices=Category.choices,
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_opened = models.DateField()
    date_closed = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name