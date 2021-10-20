from rest_framework import serializers
from inventory.models import Item, Box
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
   class Meta:
       model = Item
       fields = ('item_name', 'box', 'date_posted', 'author')


class BoxSerializer(serializers.ModelSerializer):
   class Meta:
       model = Box
       fields = ('box_name', 'box_number', 'piso', 'date_created', 'author')

'''
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       #fields = ('name', 'classification', 'language')
'''