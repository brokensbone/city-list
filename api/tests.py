from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from places.factories import BusinessFactory
import datetime

class APITests(APITestCase):
    def test_status_endpoint(self):
        """
        Ensures the status endpoint returns a 200 status code and expected data.
        """
        url = reverse('api:status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')
        self.assertTrue('timestamp' in response.data)

    def test_businesses_endpoint_lists_open_businesses(self):
        """
        Ensures the businesses endpoint returns only open businesses.
        """
        # Create one open and one closed business
        BusinessFactory(name="Open Cafe", date_closed=None)
        BusinessFactory(name="Closed Cafe", date_closed=datetime.date.today())

        url = reverse('api:business-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Open Cafe')