import pytest
from django.test import TestCase
from .models import Vendor, Item
# from django.core.exceptions import ValidationError

def test_pytest_working():
    assert True == True

class VendorModelTest(TestCase):

    def test_model_creation(self):
        vendor = Vendor.objects.create(name= "Ba-Nom-a-nom",
        phone_number= "970-682-4666",
        location= "72.37946, -37.87633",
        address= "2900 Market st Denver, CO 80205",
        status= False,
        hours= "5:00-9:00pm",
        description= "Best desserts you have ever had, and they happen to be vegan!",
        tags= "#desserts #vegan #healthy #fruit",
        website= "www.banomanom.com",
        img= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3hJWqZUQ1y5-opPj2noXiCtn14Gpz4dSOz5uKKAD2UvTVeWxtld49cOhCwj9O4Mcg0-I&usqp=CAU",
        wait_time= 20,
        upvote= False,
        downvote= False,
        favorited= False,
        up_rating= 0,
        down_rating= 0,
        distanceFromUser= 0)
        self.assertEqual(vendor.name, 'Ba-Nom-a-nom')
        self.assertEqual(vendor.phone_number, '970-682-4666')
        self.assertEqual(vendor.location, '72.37946, -37.87633')
        self.assertEqual(vendor.address, '2900 Market st Denver, CO 80205')
        self.assertEqual(vendor.status, False)
        self.assertEqual(vendor.hours, '5:00-9:00pm')
        self.assertEqual(vendor.description, 'Best desserts you have ever had, and they happen to be vegan!')
        self.assertEqual(vendor.tags, '#desserts #vegan #healthy #fruit')
        self.assertEqual(vendor.website, 'www.banomanom.com')
        self.assertEqual(vendor.img, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3hJWqZUQ1y5-opPj2noXiCtn14Gpz4dSOz5uKKAD2UvTVeWxtld49cOhCwj9O4Mcg0-I&usqp=CAU')
        self.assertEqual(vendor.wait_time, 20)
        self.assertEqual(vendor.upvote, False)
        self.assertEqual(vendor.downvote, False)
        self.assertEqual(vendor.favorited, False)
        self.assertEqual(vendor.up_rating, 0)
        self.assertEqual(vendor.down_rating, 0)
        self.assertEqual(vendor.distanceFromUser, 0)

    def test_model_query(self):
        vendor = Vendor.objects.create(name='Test Vendor')
        self.assertEqual(Vendor.objects.filter(name='Test Vendor').count(), 1)

class ItemModelTest(TestCase):

    def test_model_creation(self):
        vendor = Vendor.objects.create(name= "Ba-Nom-a-nom",
        phone_number= "970-682-4666",
        location= "72.37946, -37.87633",
        address= "2900 Market st Denver, CO 80205",
        status= False,
        hours= "5:00-9:00pm",
        description= "Best desserts you have ever had, and they happen to be vegan!",
        tags= "#desserts #vegan #healthy #fruit",
        website= "www.banomanom.com",
        img= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3hJWqZUQ1y5-opPj2noXiCtn14Gpz4dSOz5uKKAD2UvTVeWxtld49cOhCwj9O4Mcg0-I&usqp=CAU",
        wait_time= 20,
        upvote= False,
        downvote= False,
        favorited= False,
        up_rating= 0,
        down_rating= 0,
        distanceFromUser= 0)
        item = Item.objects.create(name='Test Item', price='10', description='This is a test item.', vendor= vendor)
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.price, '10')
        self.assertEqual(item.description, 'This is a test item.')

    def test_model_query(self):
        vendor = Vendor.objects.create(name= "Ba-Nom-a-nom",
        phone_number= "970-682-4666",
        location= "72.37946, -37.87633",
        address= "2900 Market st Denver, CO 80205",
        status= False,
        hours= "5:00-9:00pm",
        description= "Best desserts you have ever had, and they happen to be vegan!",
        tags= "#desserts #vegan #healthy #fruit",
        website= "www.banomanom.com",
        img= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3hJWqZUQ1y5-opPj2noXiCtn14Gpz4dSOz5uKKAD2UvTVeWxtld49cOhCwj9O4Mcg0-I&usqp=CAU",
        wait_time= 20,
        upvote= False,
        downvote= False,
        favorited= False,
        up_rating= 0,
        down_rating= 0,
        distanceFromUser= 0)
        item = Item.objects.create(name='Test Item', price='10', description='This is a test item.', vendor= vendor)
        self.assertEqual(Item.objects.filter(name='Test Item').count(), 1)