from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

PISOS = (
    ('Turmalina','TU'),
    ('Alejandro Ferrant 2', 'AF2'),
    ('Alejandro Ferrant 3','AF3'),
    ('Tomás Bretón','TB'),
)

class Item(models.Model):
	item_name = models.CharField(max_length=100, verbose_name='Nombre del Artículo')
	box = models.IntegerField(verbose_name='Caja')
	piso = models.CharField(max_length=100, choices=PISOS, default='Turmalina', verbose_name='Piso')
	date_posted = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Publicación')
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Autor')

	def __str__(self):
		return self.item_name

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk':self.pk})