from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
	item_name = models.CharField(max_length=100)
	box = models.IntegerField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.item_name

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk':self.pk})