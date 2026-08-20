from django.test import TestCase
from .models import Customer

class CustomerModelTest(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(
            name="John Doe",
            email="john@example.com"
        )
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
