from rest_framework import serializers
from inventory.models import Item, Box
from django.contrib.auth.models import User


'''
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('username')
'''

class BoxSerializer(serializers.ModelSerializer):
   author = serializers.StringRelatedField(many=False)
   class Meta:
       model = Box
       fields = ('box_name', 'box_number', 'piso', 'date_created', 'author')

class ItemSerializer(serializers.ModelSerializer):
   author = serializers.StringRelatedField(many=False)
   box = serializers.StringRelatedField(many=False)
   class Meta:
       model = Item
       fields = ('item_name', 'box', 'date_posted', 'author')


