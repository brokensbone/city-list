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