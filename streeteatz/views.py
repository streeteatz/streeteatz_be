# from django.shortcuts import render
from django.http import JsonResponse
from .models import Vendor
from .serializers import VendorSerializer

def vendor_list(request):
  vendors = Vendor.objects.all()
  serialized_vendors = VendorSerializer(vendors, many = True)
  return JsonResponse({'data': {'attributes': serialized_vendors.data}})
# Create your views here.
