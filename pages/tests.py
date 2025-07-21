from django.test import SimpleTestCase
from django.urls import reverse


class PageViewTests(SimpleTestCase):
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