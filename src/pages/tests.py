from django.test import TestCase
from django.urls import reverse


class PageViewTests(TestCase):
    def test_home_page_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Hello, world!</h1>")

    def test_about_page_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>About us</h1>")

    def test_map_page_view(self):
        """
        Tests that the map page view returns a 200 status code,
        uses the correct template, and has the correct context.
        """
        response = self.client.get(reverse("map"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/map.html')
        self.assertTrue('lat' in response.context)
        self.assertTrue('lng' in response.context)
        self.assertTrue('zoom' in response.context)

    def test_map_page_view_with_params(self):
        """
        Tests that the map page view correctly uses query parameters.
        """
        lat = 53.8008
        lng = -1.5491
        zoom = 17
        response = self.client.get(f"{reverse('map')}?lat={lat}&lng={lng}&zoom={zoom}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/map.html')
        self.assertEqual(response.context['lat'], str(lat))
        self.assertEqual(response.context['lng'], str(lng))
        self.assertEqual(response.context['zoom'], str(zoom))