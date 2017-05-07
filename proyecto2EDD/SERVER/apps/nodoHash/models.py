# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class nodoHash(models.Model):
	nombre = models.CharField(max_length=30)
	fecha = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=30)
	hora = models.CharField(max_length=30)
	eliminado = models.BooleanField()

		