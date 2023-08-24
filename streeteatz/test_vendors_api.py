import pytest
import json
from django.test import TestCase, Client
from django.urls import reverse
from .views import vendor_list, item_list, vendor_detail
from .models import Vendor, Item
from .serializers import VendorSerializer, ItemSerializer

def test_pytest_working():
    assert True == True
    
# class TestVendorModel: <-- this is a class for pytest
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

class VendorSerializerTest(TestCase):

    def test_vendor_serializer(self):
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

class ItemSerializerTest(TestCase):

    def test_item_serializer(self):
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
        vendor_1 = Vendor.objects.create(name= 'Vendor 1')
        vendor_2 = Vendor.objects.create(name= 'Vendor 2')
        serialized_vendors = VendorSerializer(Vendor.objects.all(), many=True)
        response = vendor_list(self.client)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'data': {'attributes': serialized_vendors.data}})


class ItemListViewTest(TestCase):

    def test_item_list(self):
        vendor = Vendor.objects.create(name= "Vendor 1")
        item_1 = Item.objects.create(name='Item 1', price=10, vendor=vendor)
        item_2 = Item.objects.create(name='Item 2', price=20, vendor=vendor)
        serialized_items = ItemSerializer(Item.objects.all(), many=True)
        response = item_list(self.client)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'data': {'attributes': serialized_items.data}})

class VendorDetailViewTest(TestCase):

    def test_vendor_detail(self):
        vendor = Vendor.objects.create(name='Vendor 1')
        serialized_vendor = VendorSerializer(vendor)
        response = vendor_detail(self.client, vendor_id=vendor.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'data': {'attributes': serialized_vendor.data}})

class UrlsTest(TestCase):

    def test_vendor_list_url(client):
        client = Client()
        url = reverse('vendors')
        response = client.get(url)
        assert response.status_code == 200

    def test_item_list_url(client):
        client = Client()
        url = reverse('items')
        response = client.get(url)
        assert response.status_code == 200

    def test_vendor_detail_url(client):
        vendor = Vendor.objects.create(name="Vendor 1")
        vendor.save()
        vendor_id = vendor.id
        client = Client()
        url = reverse('vendor_detail', args=[vendor_id])
        response = client.get(url)
        assert response.status_code == 200