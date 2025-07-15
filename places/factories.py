import factory
from factory.django import DjangoModelFactory
from .models import Business, BusinessGroup

class BusinessGroupFactory(DjangoModelFactory):
    class Meta:
        model = BusinessGroup
    
    name = factory.Faker('company')

class BusinessFactory(DjangoModelFactory):
    class Meta:
        model = Business

    name = factory.Faker('company')
    business_group = factory.SubFactory(BusinessGroupFactory)
    category = factory.Iterator([choice[0] for choice in Business.Category.choices])
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    date_opened = factory.Faker('date_between', start_date='-10y', end_date='today')
    date_closed = None
    notes = factory.Faker('paragraph')
