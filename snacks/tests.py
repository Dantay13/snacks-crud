from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnackModelTestCase(TestCase):
    def setUp(self):
        self.snack = Snack.objects.create(
            title="Test Snack",
            purchaser="John Doe",
            description="A tasty test snack."
        )

    def test_snack_creation(self):
        self.assertEqual(self.snack.title, "Test Snack")
        self.assertEqual(self.snack.purchaser, "John Doe")
        self.assertEqual(self.snack.description, "A tasty test snack.")

    def test_snack_string_representation(self):
        self.assertEqual(str(self.snack), self.snack.title)


class SnackListViewTestCase(TestCase):
    def setUp(self):
        self.snack = Snack.objects.create(
            title="Test Snack",
            purchaser="John Doe",
            description="A tasty test snack."
        )
        self.url = reverse("snack_list")

    def test_snack_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Snack")
        self.assertTemplateUsed(response, "snacks/snack_list.html")


class SnackDetailViewTestCase(TestCase):
    def setUp(self):
        self.snack = Snack.objects.create(
            title="Test Snack",
            purchaser="John Doe",
            description="A tasty test snack."
        )
        self.url = reverse("snack_detail", args=[self.snack.pk])

    def test_snack_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Snack")
        self.assertTemplateUsed(response, "snacks/snack_detail.html")
