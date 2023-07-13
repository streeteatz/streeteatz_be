from rest_framework.test import APITestCase
import pytest
from django.test import TestCase
from .models import Vendor, Item

class VendorModelTest(TestCase):

    def test_model_creation(self):
        vendor = Vendor.objects.create(name='Test Vendor')
        self.assertEqual(vendor.name, 'Test Vendor')

    def test_model_validation(self):
        with self.assertRaises(ValidationError):
            Vendor.objects.create(name='')

    def test_model_query(self):
        vendor = Vendor.objects.create(name='Test Vendor')
        self.assertEqual(Vendor.objects.filter(name='Test Vendor').count(), 1)

class ItemModelTest(TestCase):

    def test_model_creation(self):
        item = Item.objects.create(name='Test Item', price='10', description='This is a test item.')
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.price, '10')
        self.assertEqual(item.description, 'This is a test item.')

    def test_model_validation(self):
        with self.assertRaises(ValidationError):
            Item.objects.create(name='', price='', description='')

    def test_model_query(self):
        item = Item.objects.create(name='Test Item', price='10', description='This is a test item.')
        self.assertEqual(Item.objects.filter(name='Test Item').count(), 1)


