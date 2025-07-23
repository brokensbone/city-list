from django.core.exceptions import ValidationError
from django.test import TestCase
from ..factories import BusinessFactory, LocationFactory

class LocationModelTests(TestCase):
    def test_valid_location_succeeds(self):
        """
        Ensures a location with valid coordinates can be saved.
        """
        try:
            LocationFactory(latitude=53.8, longitude=-1.5)
        except ValidationError:
            self.fail("ValidationError was raised unexpectedly.")

    def test_invalid_latitude_fails(self):
        """
        Ensures a location with an invalid latitude raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            LocationFactory(latitude=0, longitude=-1.5)

    def test_invalid_longitude_fails(self):
        """
        Ensures a location with an invalid longitude raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            LocationFactory(latitude=53.8, longitude=0)

class BusinessModelTests(TestCase):
    def test_business_creation_with_location(self):
        """
        Tests that a Business is correctly associated with a Location.
        """
        location = LocationFactory()
        business = BusinessFactory(location=location)
        self.assertEqual(business.location, location)
        self.assertIsNotNone(business.location.latitude)
        self.assertIsNotNone(business.location.longitude)
