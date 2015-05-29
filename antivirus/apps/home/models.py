from django.db import models

class antivirus(models.Model):
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=150)
	