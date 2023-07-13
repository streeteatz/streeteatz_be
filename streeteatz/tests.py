from rest_framework.test import APITestCase


import pytest
from django.test import TestCase
from .views import vendor_list, item_list
from .models import Vendor, Item
from .serializers import VendorSerializer, ItemSerializer
from django.urls import reverse

def test_vendor_serializer(vendor_data):
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
    serializer = VendorSerializer(vendor)
    data = serializer.data
    assert data['id'] == vendor.id
    assert data['name'] == vendor.name
    assert data['phone_number'] == vendor.phone_number
    assert data['location'] == vendor.location
    assert data['address'] == vendor.address
    assert data['status'] == vendor.status
    assert data['hours'] == vendor.hours
    assert data['description'] == vendor.description
    assert data['tags'] == vendor.tags
    assert data['website'] == vendor.website
    assert data['img'] == vendor.img
    assert data['wait_time'] == vendor.wait_time
    assert data['upvote'] == vendor.upvote
    assert data['downvote'] == vendor.downvote
    assert data['favorited'] == vendor.favorited
    assert data['up_rating'] == vendor.up_rating
    assert data['down_rating'] == vendor.down_rating
    assert data['distanceFromUser'] == vendor.distanceFromUser

def test_item_serializer(item_data):
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
    serializer = ItemSerializer(item)
    data = serializer.data
    assert data['id'] == item.id
    assert data['name'] == item.name
    assert data['price'] == item.price
    assert data['description'] == item.description
    assert data['vendor'] == item.vendor.id

class VendorListViewTest(TestCase):

    def test_vendor_list(self):
        vendor_1 = Vendor.objects.create(name='Vendor 1')
        vendor_2 = Vendor.objects.create(name='Vendor 2')
        serialized_vendors = VendorSerializer(Vendor.objects.all(), many=True)
        response = vendor_list(self.client)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['attributes'], serialized_vendors.data)

class ItemListViewTest(TestCase):

    def test_item_list(self):
        item_1 = Item.objects.create(name='Item 1', price=10)
        item_2 = Item.objects.create(name='Item 2', price=20)
        serialized_items = ItemSerializer(Item.objects.all(), many=True)
        response = item_list(self.client)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['attributes'], serialized_items.data)

class UrlsTest(TestCase):

    def test_vendor_list_url(self):
        url = reverse('vendor_list')
        self.assertEqual(url, '/vendors/')

    def test_item_list_url(self):
        url = reverse('item_list')
        self.assertEqual(url, '/items/')