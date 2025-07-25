from django.test import TestCase
from django.urls import reverse
from .factories import BusinessFactory, BusinessGroupFactory

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