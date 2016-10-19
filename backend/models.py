from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Sexo(models.Model):
	valor = models.CharField(max_length=50)
	def __unicode__(self):
		return str(self.valor)

class Perfiles(models.Model):
	fecha_de_nac = models.DateField(auto_now=False,auto_now_add=False, blank=True)
	usuario = models.ForeignKey(User)
	sexo = models.ForeignKey(Sexo)
	def __unicode__(self):
		return str(self.usuario)
	class Meta:
		verbose_name_plural = "Perfiles"

class Categorias(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=500)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Categorias"

class Pais(models.Model):
	nombre = models.CharField(max_length=255)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Paises"

class Ciudades(models.Model):
	nombre = models.CharField(max_length=255)
	pais = models.ForeignKey(Pais)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Ciudades"

class Lugares(models.Model):
	categoria = models.ForeignKey(Categorias)
	ciudad = models.ForeignKey(Ciudades)
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	icono = models.CharField(max_length=255)
	portada = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=500)
	sitio_web = models.CharField(max_length=500)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, blank=True)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Lugares"

class Rutas(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=500)
	lugares = models.ManyToManyField(Lugares)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Rutas"

class Coordenadas(models.Model):
	latitude = models.CharField(max_length=255)
	longitude = models.CharField(max_length=255)
	lugar = models.ForeignKey(Lugares)
	def __unicode__(self):
		return str(self.lugar)
	class Meta:
		verbose_name_plural = "Coordenadas"

class Ranking(models.Model):
	lugar = models.ForeignKey(Lugares)
	usuario = models.ForeignKey(User)
	valor = models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.lugar)
	class Meta:
		verbose_name_plural = "Ranking"

class Roles(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=500)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = "Roles"

class Permisos(models.Model):
	lugar = models.ForeignKey(Lugares)
	usuario = models.ForeignKey(User)
	rol = models.ForeignKey(Roles)
	def __unicode__(self):
		return str(self.usuario)
	class Meta:
		verbose_name_plural = "Permisos"

class Galerias(models.Model):
	nombre = models.CharField(max_length=255)
	alt = models.CharField(max_length=255)
	path = models.CharField(max_length=255)
	def __unicode__(self):
		return str(self.nombre)
	class Meta:
		verbose_name_plural = u'Galerias'

class RedesSociales(models.Model):
	lugar = models.ForeignKey(Lugares)
	link = models.CharField(max_length=255)
	def __unicode__(self):
		return str(self.lugar)
	class Meta:
		verbose_name_plural = "Redes Sociales"

class Tag(models.Model):
	valor = models.CharField(max_length=255)
	lugar = models.ForeignKey(Lugares)
	def __unicode__(self):
		return str(self.lugar)

class Email(models.Model):
	valor = models.EmailField(max_length=100, unique= True)
	lugar = models.ForeignKey(Lugares)
	perfil = models.ForeignKey(Perfiles)
	def __unicode__(self):
		return str(self.valor)

class Telefonos(models.Model):
	valor = models.IntegerField()
	lugar = models.ForeignKey(Lugares)
	perfil = models.ForeignKey(Perfiles)
	def __unicode__(self):
		return str(self.valor)
	class Meta:
		verbose_name_plural = "Telefonos"
