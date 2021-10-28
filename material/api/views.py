from django.shortcuts import render
from inventory.models import Item, Box
from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import ItemSerializer, BoxSerializer#, UserSerializer


class ItemsViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	http_method_names = ['get']

class BoxViewSet(viewsets.ModelViewSet):
	queryset = Box.objects.all()
	serializer_class = BoxSerializer
	http_method_names = ['get']

'''
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
'''