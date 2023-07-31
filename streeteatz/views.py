# from django.shortcuts import render
from django.http import JsonResponse
from django.rest_framework import Response
from .models import Vendor
from .models import Item
from .serializers import VendorSerializer
from .serializers import ItemSerializer

def vendor_list(request):
  vendors = Vendor.objects.all()
  serialized_vendors = VendorSerializer(vendors, many = True)
  return JsonResponse({'data': {'attributes': serialized_vendors.data}})
  # return Response(serialized_vendors.data)

def item_list(request):
  items = Item.objects.all()
  serialized_items = ItemSerializer(items, many = True)
  return JsonResponse({'data': {'attributes': serialized_items.data}})

def vendor_detail(request, vendor_id):
  vendor = Vendor.objects.get(id = vendor_id)
  serialized_vendor = VendorSerializer(vendor)
  return JsonResponse({'data': {'attributes': serialized_vendor.data}})
# Create your views here.
