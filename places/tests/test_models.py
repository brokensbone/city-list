from django.core.exceptions import ValidationError
from django.test import TestCase
from ..factories import BusinessFactory

class BusinessModelTests(TestCase):
    def test_valid_business_succeeds(self):
        """
        Ensures a business with valid coordinates can be saved.
        """
        try:
            BusinessFactory(latitude=53.8, longitude=-1.5)
        except ValidationError:
            self.fail("ValidationError was raised unexpectedly.")

    def test_invalid_latitude_fails(self):
        """
        Ensures a business with an invalid latitude raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            BusinessFactory(latitude=0, longitude=-1.5)

    def test_invalid_longitude_fails(self):
        """
        Ensures a business with an invalid longitude raises a ValidationError.
        """
        with self.assertRaises(ValidationError):
            BusinessFactory(latitude=53.8, longitude=0)
