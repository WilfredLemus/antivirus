from django.db import models

class Categoria(models.Model):

	nombre = models.CharField(max_length=50)
	slug = models.SlugField(editable=False)

	def save(self,*args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre


class antivirus(models.Model):
	nombre = models.CharField(max_length=100)
	slug = models.SlugField(editable=False)
	descripcion = models.CharField(max_length=150)
	imagen = models.ImageField(upload_to = 'ImgAntivirus')
	precio = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	categoria = models.ForeignKey(Categoria)
	SistemaOperativo = models.CharField(max_length=60)
	arquitectura = models.CharField(max_length=60)
	ram = models.IntegerField()


	# def save(self, *args, **kwargs):
	# 	if not self.id:
	# 		self.slug = slugify(self.nombre)
	# 	super(antivirus, self).save(*args, **kwargs)

	# def __unicode__(self):
	# 	return self.nombre