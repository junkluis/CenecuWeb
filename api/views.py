# -*- coding: utf-8 -*-
"""Vistas de CRUD api"""

from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import Horario, Curso, Profesor, CursoProfesor, Area, Anuncio
from .models import Frase, GoalsList, AreaInteres, UsuarioRol, Nota
from .models import ContenidoCompartido, RegistroUsuarioCurso, Telefonos
from django.forms.models import model_to_dict
from django.utils.encoding import python_2_unicode_compatible


def apiIndex(request):
    modelos = ['Horario', 'Curso', 'Profesor', 'CursoProfesor', 'Area',
               'Anuncio', 'Frase', 'GoalsList', 'AreaInteres', 'UsuarioRol',
               'Nota', 'ContenidoCompartido', 'RegistroUsuarioCurso',
               'Telefonos']

    respuesta = {'modelos': modelos}
    return render(request, 'api/index.html', respuesta)


def error_404(request):
    data = {}
    return render(request, 'api/error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'api/error_500.html', data)


class HorarioView(generics.ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

    def perform_create(self, serializer):
        serializer.save()


class CursoView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProfesorView(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def perform_create(self, serializer):
        serializer.save()


class CursoProfesorView(generics.ListCreateAPIView):
    queryset = CursoProfesor.objects.all()
    serializer_class = CursoProfesorSerializer

    def perform_create(self, serializer):
        serializer.save()


class AreaView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def perform_create(self, serializer):
        serializer.save()


class AnuncioView(generics.ListCreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def perform_create(self, serializer):
        serializer.save()


class FraseView(generics.ListCreateAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer

    def perform_create(self, serializer):
        serializer.save()


class GoalsListView(generics.ListCreateAPIView):
    queryset = GoalsList.objects.all()
    serializer_class = GoalsListSerializer

    def perform_create(self, serializer):
        serializer.save()


class AreaInteresView(generics.ListCreateAPIView):
    queryset = AreaInteres.objects.all()
    serializer_class = AreaInteresSerializer

    def perform_create(self, serializer):
        serializer.save()


class UsuarioRolView(generics.ListCreateAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer

    def perform_create(self, serializer):
        serializer.save()


class NotaView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    def perform_create(self, serializer):
        serializer.save()


class ContenidoCompartidoView(generics.ListCreateAPIView):
    queryset = ContenidoCompartido.objects.all()
    serializer_class = ContenidoCompartidoSerializer

    def perform_create(self, serializer):
        serializer.save()


class RegistroUsuarioCursoView(generics.ListCreateAPIView):
    queryset = RegistroUsuarioCurso.objects.all()
    serializer_class = RegistroUsuarioCursoSerializer

    def perform_create(self, serializer):
        serializer.save()


class TelefonosView(generics.ListCreateAPIView):
    queryset = Telefonos.objects.all()
    serializer_class = TelefonosSerializer

    def perform_create(self, serializer):
        serializer.save()


class HorarioEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class CursoEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ProfesorEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


class CursoProfesorEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = CursoProfesor.objects.all()
    serializer_class = CursoProfesorSerializer


class AreaEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AnuncioEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer


class FraseEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Frase.objects.all()
    serializer_class = FraseSerializer


class GoalsListEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoalsList.objects.all()
    serializer_class = GoalsListSerializer


class AreaInteresEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaInteres.objects.all()
    serializer_class = AreaInteresSerializer


class UsuarioRolEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer


class NotaEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


class ContenidoCompartidoEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContenidoCompartido.objects.all()
    serializer_class = ContenidoCompartidoSerializer


class RegistroUsuarioCursoEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistroUsuarioCurso.objects.all()
    serializer_class = RegistroUsuarioCursoSerializer


class TelefonosEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telefonos.objects.all()
    serializer_class = TelefonosSerializer


@apiView(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        username = 'testUser'
        password = 'Password123'
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"user": user.username})
        else:
            return Response({"user": "you are not my dad"})
    else:
        return Response({"message": "Hello, world!"})


# login API
@apiView(['GET', 'POST'])
def loginCenecu(request):

    context = {}

    if request.method == 'POST':
        print(request.data)
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            userRol = UsuarioRol.objects.get(usuarioId=user.pk)
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


# Notas por usuario
@apiView(['GET'])
def notasPorUser(request, pk):

    listaNotas = []

    notasUser = Nota.objects.all().filter(usuarioId=pk)
    print(notasUser)
    for nota in notasUser:
        listaNotas.append(model_to_dict(nota))

    return Response(listaNotas)


@apiView(['GET'])
def borrarNota(request, pk):

    notaBorrar = Nota.objects.get(id=pk)
    if notaBorrar is not None:
        notaBorrar.delete()
        return Response({'msg': 'La nota se eliminó con exito'})
    else:
        return Response({'msg': 'err'})


@apiView(['POST'])
def registrarUsuario(request):

    username = request.data["user"]
    password = request.data["pass"]
    apellido = request.data["apellido"]
    nombre = request.data["nombre"]
    email = request.data["email"]

    try:
        extUser = User.objects.get(username=username)
    except User.DoesNotExist:
        extUser = None

    if extUser is None:
        if username != "" and password != "" and email != "":
            user = User.objects.create_user(username, email, password)
            if nombre != "":
                user.first_name = nombre
            if apellido != "":
                user.last_name = apellido
            user.save()
            return Response(model_to_dict(user))
        else:
            return Response({'msg': 'err'})
    else:
        return Response({'msg': 'extUser'})


@apiView(['GET'])
def logOut(request):
    logout(request)
    return Response({'msg': 'logOut'})
