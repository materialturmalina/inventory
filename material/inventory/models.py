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


class Box(models.Model):
	box_name = models.CharField(max_length=100, verbose_name='Nombre de la Caja')
	box_number = models.IntegerField(verbose_name='Número de la Caja')
	piso = models.CharField(max_length=100, choices=PISOS, default='Turmalina', verbose_name='Piso')
	date_created = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Autor')
	
	class Meta:
			unique_together = ["box_number", "piso"]
	
	def unique_error_message(self, model_class, unique_check):
		if model_class == type(self) and unique_check == ('box_number', 'piso'):
			return 'Ya existe una caja con ese número en el piso seleccionado'
		else:
			return super(Box, self).unique_error_message(model_class, unique_check)

	def __str__(self):
		return str(self.box_number) + ": " + self.box_name + " (" + self.piso + ")"

	def get_absolute_url(self):
		return reverse('box-detail', kwargs={'pk':self.pk})

class Item(models.Model):
	item_name = models.CharField(max_length=100, verbose_name='Nombre del Artículo')
	box = models.ForeignKey(Box, null=True, on_delete=models.CASCADE, verbose_name='Caja')
	date_posted = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Publicación')
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Autor')

	def __str__(self):
		return self.item_name

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk':self.pk})


