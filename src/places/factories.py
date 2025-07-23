import factory
from factory.django import DjangoModelFactory
from .models import Business, BusinessGroup, Location
from django.conf import settings

class BusinessGroupFactory(DjangoModelFactory):
    class Meta:
        model = BusinessGroup
    
    name = factory.Faker('company')

class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    latitude = factory.Faker(
        'pyfloat',
        min_value=float(settings.MAP_BOUNDS_MIN_LAT),
        max_value=float(settings.MAP_BOUNDS_MAX_LAT)
    )
    longitude = factory.Faker(
        'pyfloat',
        min_value=float(settings.MAP_BOUNDS_MIN_LNG),
        max_value=float(settings.MAP_BOUNDS_MAX_LNG)
    )
    address = factory.Faker('address')

class BusinessFactory(DjangoModelFactory):
    class Meta:
        model = Business

    name = factory.Faker('company')
    business_group = factory.SubFactory(BusinessGroupFactory)
    location = factory.SubFactory(LocationFactory)
    category = factory.Iterator([choice[0] for choice in Business.Category.choices])
    date_opened = factory.Faker('date_between', start_date='-10y', end_date='today')
    date_closed = None
    notes = factory.Faker('paragraph')
