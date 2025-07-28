from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .factories import BusinessFactory, BusinessGroupFactory, LocationFactory
from .models import Location

User = get_user_model()

class BusinessViewTests(TestCase):
    def test_business_list_view(self):
        """
        Tests that the business list view returns a 200 status code,
        uses the correct template, and displays businesses.
        """
        # Create a few businesses to test with
        business_a = BusinessFactory(name="Aardvark Cafe")
        business_c = BusinessFactory(name="Cobra Cafe")
        business_b = BusinessFactory(name="Badger Cafe")

        response = self.client.get(reverse('places:business-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/business_list.html')
        self.assertContains(response, "Aardvark Cafe")
        self.assertContains(response, "Badger Cafe")
        self.assertContains(response, "Cobra Cafe")

        # Check that the businesses are ordered alphabetically
        businesses_in_context = list(response.context['businesses'])
        self.assertEqual(businesses_in_context[0], business_a)
        self.assertEqual(businesses_in_context[1], business_b)
        self.assertEqual(businesses_in_context[2], business_c)

    def test_business_detail_view(self):
        """
        Tests that the business detail view returns a 200 status code,
        uses the correct template, and displays the correct business details.
        """
        business = BusinessFactory()
        response = self.client.get(reverse('places:business-detail', kwargs={'pk': business.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/business_detail.html')
        self.assertContains(response, business.name)
        self.assertContains(response, business.business_group.name)
        self.assertContains(response, business.get_category_display())

class BusinessGroupViewTests(TestCase):
    def test_business_group_detail_view(self):
        """
        Tests that the business group detail view returns a 200 status code,
        uses the correct template, and displays the correct businesses.
        """
        business_group = BusinessGroupFactory()
        business_a = BusinessFactory(business_group=business_group, name="Aardvark Cafe")
        business_c = BusinessFactory(business_group=business_group, name="Cobra Cafe")
        business_b = BusinessFactory(business_group=business_group, name="Badger Cafe")

        # Create a business in a different group to ensure it's not displayed
        other_group = BusinessGroupFactory()
        BusinessFactory(business_group=other_group, name="Don't Show Me")

        response = self.client.get(reverse('places:business-group-detail', kwargs={'pk': business_group.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'places/business_group_detail.html')
        self.assertContains(response, business_group.name)
        self.assertContains(response, "Aardvark Cafe")
        self.assertContains(response, "Badger Cafe")
        self.assertContains(response, "Cobra Cafe")
        self.assertNotContains(response, "Don't Show Me")

        # Check that the businesses are ordered alphabetically
        businesses_in_context = list(response.context['businesses'])
        self.assertEqual(businesses_in_context[0], business_a)
        self.assertEqual(businesses_in_context[1], business_b)
        self.assertEqual(businesses_in_context[2], business_c)

class LocationAdminTests(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'admin', 'admin@example.com', 'password'
        )
        self.client.login(username='admin', password='password')
        self.location = LocationFactory()

    def test_location_add_view(self):
        """
        Tests that the location add view loads correctly and contains the map widget.
        """
        url = reverse('admin:places_location_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/places/location/change_form.html')
        self.assertContains(response, 'leaflet.css')
        self.assertContains(response, 'leaflet.js')
        self.assertContains(response, '<div id="map"')

    def test_location_change_view(self):
        """
        Tests that the location change view loads correctly and contains the map widget.
        """
        url = reverse('admin:places_location_change', args=[self.location.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/places/location/change_form.html')
        self.assertContains(response, 'leaflet.css')
        self.assertContains(response, 'leaflet.js')
        self.assertContains(response, '<div id="map"')

    def test_location_form_save(self):
        """
        Tests that the location form correctly saves the latitude and longitude.
        """
        url = reverse('admin:places_location_add')
        data = {
            'latitude': '53.8',
            'longitude': '-1.5',
            'address': '123 Test Street',
            'business_set-TOTAL_FORMS': '1',
            'business_set-INITIAL_FORMS': '0',
            'business_set-MIN_NUM_FORMS': '0',
            'business_set-MAX_NUM_FORMS': '1000',
            'business_set-0-name': '',
            'business_set-0-business_group': '',
            'business_set-0-category': '',
            'business_set-0-date_opened': '',
            'business_set-0-date_closed': '',
            'business_set-0-notes': '',
            'business_set-0-DELETE': '',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect and check for the success message
        response = self.client.get(response.url)
        self.assertContains(response, "was added successfully.")

        # Check that the location was created with the correct data
        location = Location.objects.get(address='123 Test Street')
        self.assertEqual(location.latitude, 53.8)
        self.assertEqual(location.longitude, -1.5)
