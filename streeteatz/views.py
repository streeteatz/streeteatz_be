# from django.shortcuts import render
from django.http import JsonResponse
from .models import Vendor
from .models import Item
from .serializers import VendorSerializer
from .serializers import ItemSerializer

def vendor_list(request):
  vendors = Vendor.objects.all()
  serialized_vendors = VendorSerializer(vendors, many = True)
  return JsonResponse({'data': {'attributes': serialized_vendors.data}})

def item_list(request):
  items = Item.objects.all()
  serialized_items = ItemSerializer(items, many = True)
  return JsonResponse({'data': {'attributes': serialized_items.data}})
# Create your views here.
