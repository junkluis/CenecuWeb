from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
	nombre = models.CharField(max_length = 100, blank = False)
	descripcion = models.CharField(max_length = 255)
	urlPensum = models.CharField(max_length = 255)
	duracion = models.IntegerField()
	costo = models.FloatField()
	imgCurso = models.CharField(max_length = 255, blank = False)
	horario = models.CharField(max_length = 100, blank = False)
	estado = models.CharField(max_length = 50, blank = False)

	def __str__(self):
		return "{}".format(self.nombre)


class CursoProfesor(models.Model):
	cursoId = models.ForeignKey('curso', on_delete=models.CASCADE)
	profesorId = models.ForeignKey('profesor', on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.cursoId)


class Profesor(models.Model):
	nombre = models.CharField(max_length = 10, blank = False)
	apellido = models.CharField(max_length = 10, blank = False)
	titulo = models.CharField(max_length = 50)
	imgPerfil = models.CharField(max_length = 255)
	frasePersonal = models.CharField(max_length = 100)
	descripcion = models.CharField(max_length = 255)
	areaEspecializacion = models.ForeignKey('area', on_delete=models.CASCADE)
	urlLinkedin = models.CharField(max_length = 255)
	urlCurriculum = models.CharField(max_length = 255)
	estado = models.CharField(max_length = 50)

	def __str__(self):
		return "{}".format(self.nombre)


class Area(models.Model):
	nombre = models.CharField(max_length = 50, blank = False)
	descripcion = models.CharField(max_length = 255)
	imgArea = models.CharField(max_length = 255)
	estado = models.CharField(max_length = 50)	

	def __str__(self):
		return "{}".format(self.nombre)


class AreaInteres(models.Model):
	usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
	areaId = models.ForeignKey('area', on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.usuarioId)


class UsuarioRol(models.Model):
	usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
	rol = models.CharField(max_length=50, blank=False)

	def __str__(self):
		return "{}".format(self.usuarioId)


class Nota(models.Model):
	titulo = models.CharField(max_length=50, blank=False)
	descripion = models.CharField(max_length=255)
	fechaLimite = models.DateField()
	notificacion = models.BooleanField()
	icono = models.CharField(max_length = 255)
	usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.titulo)


class GoalsList(models.Model):
	usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
	cursoId = models.ForeignKey('curso', on_delete=models.CASCADE)
	estado = models.CharField(max_length = 50)	

	def __str__(self):
		return "{}".format(self.usuarioId)


class Frase(models.Model):
	descripcion = models.CharField(max_length =250)
	imgFrase = models.CharField(max_length = 255)
	estado = models.CharField(max_length = 50)

	def __str__(self):
		return "{}".format(self.descripcion)


class Anuncio(models.Model):
	descripcion = models.CharField(max_length =250)
	imgAnuncio = models.CharField(max_length = 255)
	urlAnuncio = models.CharField(max_length = 255)
	estado = models.CharField(max_length = 50)

	def __str__(self):
		return "{}".format(self.descripcion)


class BolsaDeTrabajo(models.Model):
	titulo = models.CharField(max_length =100)
	descripcion = models.CharField(max_length =250)
	estado = models.CharField(max_length = 50)
	
	def __str__(self):
		return "{}".format(self.descripcion)


class UsuariosTrabajo(models.Model):
	usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
	bolsaDeTrabajoId = models.ForeignKey('bolsaDeTrabajo', on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.usuarioId)

