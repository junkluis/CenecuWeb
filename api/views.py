## -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import *
from django.forms.models import model_to_dict
from django.utils.encoding import python_2_unicode_compatible


class CursoView(generics.ListCreateAPIView):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer

	def perform_create(self, serializer):
		serializer.save()


class CursoEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer
	

class CursoProfesorView(generics.ListCreateAPIView):
	queryset = CursoProfesor.objects.all()
	serializer_class = CursoProfesorSerializer

	def perform_create(self, serializer):
		serializer.save()


class CursoProfesorEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = CursoProfesor.objects.all()
	serializer_class = CursoProfesorSerializer
	

class ProfesorView(generics.ListCreateAPIView):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer

	def perform_create(self, serializer):
		serializer.save()


class ProfesorEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer
	

class AreaView(generics.ListCreateAPIView):
	queryset = Area.objects.all()
	serializer_class = AreaSerializer

	def perform_create(self, serializer):
		serializer.save()


class AreaEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = Area.objects.all()
	serializer_class = AreaSerializer
	

class AreaInteresView(generics.ListCreateAPIView):
	queryset = AreaInteres.objects.all()
	serializer_class = AreaInteresSerializer

	def perform_create(self, serializer):
		serializer.save()


class AreaInteresEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = AreaInteres.objects.all()
	serializer_class = AreaInteresSerializer
	

class UsuarioRolView(generics.ListCreateAPIView):
	queryset = UsuarioRol.objects.all()
	serializer_class = UsuarioRolSerializer

	def perform_create(self, serializer):
		serializer.save()


class UsuarioRolEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = UsuarioRol.objects.all()
	serializer_class = UsuarioRolSerializer
	

class NotaView(generics.ListCreateAPIView):
	queryset = Nota.objects.all()
	serializer_class = NotaSerializer

	def perform_create(self, serializer):
		serializer.save()


class NotaEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = Nota.objects.all()
	serializer_class = NotaSerializer
	

class GoalsListView(generics.ListCreateAPIView):
	queryset = GoalsList.objects.all()
	serializer_class = GoalsListSerializer

	def perform_create(self, serializer):
		serializer.save()


class GoalsListEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = GoalsList.objects.all()
	serializer_class = GoalsListSerializer
	

class FraseView(generics.ListCreateAPIView):
	queryset = Frase.objects.all()
	serializer_class = FraseSerializer

	def perform_create(self, serializer):
		serializer.save()


class FraseEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = Frase.objects.all()
	serializer_class = FraseSerializer
	

class AnuncioView(generics.ListCreateAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer

	def perform_create(self, serializer):
		serializer.save()


class AnuncioEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = Anuncio.objects.all()
	serializer_class = AnuncioSerializer
	

class BolsaDeTrabajoView(generics.ListCreateAPIView):
	queryset = BolsaDeTrabajo.objects.all()
	serializer_class = BolsaDeTrabajoSerializer

	def perform_create(self, serializer):
		serializer.save()


class BolsaDeTrabajoEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = BolsaDeTrabajo.objects.all()
	serializer_class = BolsaDeTrabajoSerializer
	

class UsuariosTrabajoView(generics.ListCreateAPIView):
	queryset = UsuariosTrabajo.objects.all()
	serializer_class = UsuariosTrabajoSerializer

	def perform_create(self, serializer):
		serializer.save()


class UsuariosTrabajoEdit(generics.RetrieveUpdateDestroyAPIView):
	queryset = UsuariosTrabajo.objects.all()
	serializer_class = UsuariosTrabajoSerializer
	


@api_view(['GET', 'POST'])
def hello_world(request):
	if request.method == 'POST':
		username = 'luis'
		password = 'Batman123'
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return Response({"user": user.username})
		else:
			return Response({"user": "you are not my dad"})
	else:
		return Response({"message": "Hello, world!"})
	

#login API
@api_view(['GET', 'POST'])
def loginCenecu(request):

	context = {}

	if request.method == 'POST':
		print(request.data)
		username = request.data["username"]
		password = request.data["password"]

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			userRol = UsuarioRol.objects.get(usuarioId = user.pk)
			context = {
				'user': model_to_dict(user),
				'rol': userRol.rol,
				'err': None
			}
			return Response(context)
		else:
			return Response({"err": "falloLogin"})
	else:
		return Response({"err": "permisosInvalidos"})


#Notas por usuario
@api_view(['GET'])
def notasPorUser(request, pk):

	context = {}
	listaNotas = []

	notasUser = Nota.objects.all().filter(usuarioId = pk)
	print(notasUser)
	for nota in notasUser:
		listaNotas.append(model_to_dict(nota))

	return Response(listaNotas);


@api_view(['GET'])
def borrarNota(request, pk):
	
	notaBorrar = Nota.objects.get(id = pk)
	if notaBorrar is not None:
		notaBorrar.delete()
		return Response({'msg':'La nota se eliminó con exito'});
	else:
		return Response({'msg': 'err'});


@api_view(['POST'])
def registrarUsuario(request):
	
	username = request.data["user"]
	password = request.data["pass"]
	apellido = request.data["apellido"]
	nombre = request.data["nombre"]
	email = request.data["email"]

	try:
		extUser = User.objects.get(username = username)
	except User.DoesNotExist:
		extUser = None

	if extUser is None:
		if username != "" and password != "" and email != "" :
			user = User.objects.create_user(username, email, password)
			if nombre != "":
				user.first_name = nombre
			if apellido != "":
				user.last_name = apellido
			user.save()
			return Response(model_to_dict(user))
		else:
			return Response({'msg': 'err'});
	else:
		return Response({'msg': 'extUser'});


@api_view(['GET'])
def logOut(request):
	logout(request)
	return Response({'msg': 'logOut'});