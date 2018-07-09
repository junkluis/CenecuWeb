from rest_framework import serializers
from .models import *


class CursoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Curso
		fields = ('pk','nombre','descripcion','urlPensum','duracion','costo','imgCurso','horario','estado')



class CursoProfesorSerializer(serializers.ModelSerializer):

	class Meta:
		model = CursoProfesor
		fields = ('pk','cursoId','profesorId')


class ProfesorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profesor
		fields = ('pk', 'nombre', 'apellido', 'titulo', 'imgPerfil', 'frasePersonal', 'descripcion', 'areaEspecializacion', 'urlLinkedin', 'urlCurriculum', 'estado')


class AreaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Area
		fields = ('pk', 'nombre', 'descripcion', 'imgArea', 'estado')



class AreaInteresSerializer(serializers.ModelSerializer):

	class Meta:
		model = AreaInteres
		fields = ('pk', 'usuarioId', 'areaId')


class UsuarioRolSerializer(serializers.ModelSerializer):

	class Meta:
		model = UsuarioRol
		fields = ('pk', 'usuarioId', 'rol')



class NotaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Nota
		fields = ('pk', 'titulo', 'descripion', 'fechaLimite', 'notificacion', 'icono', 'usuarioId' )



class GoalsListSerializer(serializers.ModelSerializer):

	class Meta:
		model = GoalsList
		fields = ('pk', 'usuarioId','cursoId','estado')



class FraseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Frase
		fields = ('pk', 'descripcion', 'imgFrase', 'estado')


class AnuncioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Anuncio
		fields = ('pk', 'descripcion', 'imgAnuncio', 'urlAnuncio', 'estado')


class BolsaDeTrabajoSerializer(serializers.ModelSerializer):

	class Meta:
		model = BolsaDeTrabajo
		fields = ('pk', 'titulo', 'descripcion', 'estado')


class UsuariosTrabajoSerializer(serializers.ModelSerializer):

	class Meta:
		model = UsuariosTrabajo
		fields = ('pk', 'usuarioId', 'bolsaDeTrabajoId')

