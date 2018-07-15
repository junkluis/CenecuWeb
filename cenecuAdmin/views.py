## -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.shortcuts import render, redirect, render_to_response

from django.http import HttpResponse

from django.shortcuts import render

from api.models import *

from django.utils.encoding import python_2_unicode_compatible

from django.template import loader

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def iniciarSesion(request):
	"""Inicia sesion en la app web del Administrador"""
	template = loader.get_template('cenecuAdmin/page-login.html/')
	
	if(request.method == 'POST'):
		usuario = request.POST.get('usuario')
		clave = request.POST.get('password')
		user = authenticate(username=usuario, password=clave)
		if (user is not None):
			usuariorol=UsuarioRol.objects.get(usuario_id=request.user.id)
			if(usuariorol.rol == "admin"):
				messages.success(request, '¡Bienvenido!')
				login(request, user)
				return redirect('/adminIndex/')
			else:
				messages.success(request, 'Acceso no autotizado')
				return redirect ('/login')

		else:
			messages.success(request, 'Usuario y/o contraseña no válidos')
			return redirect ('/login')
	else:
		notice = 'none'
	
	context = {
		'notice': notice 
	}
	return HttpResponse(template.render(context, request))
	

def cerrarSesion (request):
	"""Cierra sesion en la app web del Administrador"""	
	messages.success(request, 'Cierre de sesión exitoso')
	logout(request)
	return redirect('/login')

	
def index(request):
	"""Tras iniciar sesion, se muestra la pagina Detalle de Cursos"""
	if (request.user.is_authenticated):
		cursos = Curso.objects.all()
		context = {
			'cursos':cursos
		}
		return  render(request, "cenecuAdmin/detalles-Cursos.html", context)
	else :
		return redirect('/login')


def listarProfesores(request):
	"""Lista los profesores de la base de datos"""
	if (request.user.is_authenticated):
		profesores = Profesor.objects.all()
		context = {
			'profesores':profesores
		}
		return  render(request, "cenecuAdmin/detallesProfesores.html", context)
	else :
		return redirect('/login/')		


def crearCurso (request):
	"""Muestra la pagina para crear un nuevo curso"""
	if (request.user.is_authenticated):
		area=Area.objects.all()
		listaProfesor = Profesor.objects.all()
		print(listaProfesor)
		context = {
			'area':area,
			'listaProfesor':listaProfesor
		}
		return  render(request, "cenecuAdmin/crearCurso.html", context)
	else :
		return redirect('/login/')	


def nuevoCurso(request):
	"""Agrega un nuevo curso a la base de datos , crea relacion entre profesor y curso """
	if (request.user.is_authenticated):
		context = {
		}
		if (request.POST):
			nuevoCurso = Curso()
			nuevoCurso.nombre = request.POST.get('nombreCurso')
			nuevoCurso.descripcion = request.POST.get('descripcion')
			nuevoCurso.pensum = request.FILES.get('pensum')
			nuevoCurso.duracion_cant = request.POST.get('duracion')
			nuevoCurso.duracion_tipo = request.POST.get('tipoDuracion')
			nuevoCurso.costo = request.POST.get('costo')
			nuevoCurso.img_curso = request.FILES.get('imagen')
			areaRequerido = Area.objects.get(pk=request.POST.get('area'))
			nuevoCurso.area_estudio = areaRequerido
			nuevoCurso.estado = request.POST.get('estado')
			nuevoCurso.fecha_creado = datetime.datetime.now()
			nuevoCurso.save()
			cursoProfesor = CursoProfesor()
			cursoProfesor.curso_id = nuevoCurso
			cursoProfesor.profesor_id = Profesor.objects.get(pk=request.POST.get('profesor'))
			cursoProfesor.save()
			messages.success(request, '¡Curso creado correctamente!')
		return redirect('/adminIndex/')
	else :
		return redirect('/login/')	


def modificarCurso(request):
	"""Edita un curso que se encuentra en la base de datos"""
	if (request.user.is_authenticated):
		if (request.POST):
			idCurso = int(request.POST.get('idcurso'))
			nuevoCurso = Curso.objects.get(id=int(request.POST.get('idcurso')))
			nuevoCurso.nombre = request.POST.get('nombreCurso')
			nuevoCurso.descripcion = request.POST.get('descripcion')
			nuevoCurso.pensum = request.FILES.get('pensum')
			nuevoCurso.duracion_cant = request.POST.get('duracion')
			nuevoCurso.costo = request.POST.get('costo')
			nuevoCurso.img_curso = request.FILES.get('imgCurso')
			nuevoCurso.estado = request.POST.get('estado')
			nuevoCurso.fecha_creado = datetime.datetime.now()
			nuevoCurso.save()
			messages.success(request, '¡Curso modificado correctamente!')
		return redirect ('/adminIndex/')
	else :
		return redirect('/login/')	


def editarCurso(request,pk):
	"""Muestra la pagina para editar un curso"""
	if (request.user.is_authenticated):
		idcurso = pk
		listaProfesores = Profesor.objects.all()
		listaArea = Area.objects.all()
		cursoRequerido = Curso.objects.get(pk=pk)
		cursoProfesor = CursoProfesor.objects.get(curso_id=cursoRequerido.pk)
		nombreProfesor = cursoProfesor.profesor_id
		nombre = cursoRequerido.nombre
		descripcion = cursoRequerido.descripcion
		urlPensum = cursoRequerido.pensum
		duracion = cursoRequerido.duracion_cant
		duracion_tipo = cursoRequerido.duracion_tipo
		costo = cursoRequerido.costo
		imgCurso = cursoRequerido.img_curso
		
		estado = cursoRequerido.estado
		areaRequerido = Area.objects.get(pk=cursoRequerido.area_estudio.pk)
		area_estudio = areaRequerido
		context = {
			'nombre':nombre,
			'descripcion': descripcion,
			'duracion': duracion,
			'duracion_tipo': duracion_tipo,
			'costo': costo,
			'profesores': listaProfesores,
			'estado': estado,
			'imgCurso': imgCurso,
			'urlPensum': urlPensum,
			'area_estudio':area_estudio,
			'listaArea':listaArea,
			'nombreProfesor': nombreProfesor,
			'idcurso': idcurso
		}
		return render(request, "cenecuAdmin/editarCurso.html", context)
	else :
		return redirect('/login/')	


def eliminarCurso(request,pk):
	"""Elimina un curso de la base de datos"""
	if (request.user.is_authenticated):
		curso = Curso.objects.get(pk = pk)
		curso.delete()
		return redirect('/adminIndex/')
	else :
		return redirect('/login/')	


def crearProfesor (request):
	"""Muestra la pagina para crear un nuevo perfil de profesor"""
	if (request.user.is_authenticated):
		areas = Area.objects.all()
		context={
			'areas': areas,
		}
		return  render(request, "cenecuAdmin/crearProfesor.html", context)
	else :
		return redirect('/login/')


def nuevoProfesor(request):
	"""Agrega un nuevo perfil de profesor a la base de datos"""
	if (request.user.is_authenticated):
		if (request.POST):
			nuevoProfesor = Profesor()
			nuevoProfesor.nombre = request.POST.get('nombreProfesor')
			nuevoProfesor.apellido = request.POST.get('apellidoProfesor')
			nuevoProfesor.titulo = request.POST.get('titulo')
			nuevoProfesor.imgPerfil = request.POST.get('imgPerfil')
			nuevoProfesor.frasePersonal = request.POST.get('frasePersonal')
			nuevoProfesor.descripcion = request.POST.get('descripcion')
			
			areaId = request.POST.get('areaEspecializacion')
			areaSelect = Area.objects.get(pk = areaId)
			nuevoProfesor.areaEspecializacion = areaSelect

			nuevoProfesor.urlLinkedin = request.POST.get('urlLinkedin')
			nuevoProfesor.urlCurriculum = request.POST.get('urlCurriculum')
			nuevoProfesor.estado = request.POST.get('estado')
			nuevoProfesor.save()
			messages.success(request, '¡Profesor creado correctamente!')
		return redirect('/listarProfesores/')
	else :
		return redirect('/login/')	


def modificarProfesor(request):
	"""Edita un perfil de profesor que se encuentra en la base de datos"""
	if (request.user.is_authenticated):
		if (request.POST):
			idProfesor = int(request.POST.get('idprofesor'))
			nuevoProfesor = Profesor.objects.get(id=int(request.POST.get('idprofesor')))
			nuevoProfesor.nombre = request.POST.get('nombreProfesor')
			nuevoProfesor.apellido = request.POST.get('apellidoProfesor')
			nuevoProfesor.titulo = request.POST.get('titulo')
			nuevoProfesor.imgPerfil = request.POST.get('imgPerfil')
			nuevoProfesor.frasePersonal = request.POST.get('frasePersonal')
			nuevoProfesor.descripcion = request.POST.get('descripcion')
			nuevoProfesor.urlLinkedin = request.POST.get('urlLinkedin')
			nuevoProfesor.urlCurriculum = request.POST.get('urlCurriculum')
			nuevoProfesor.estado = request.POST.get('estado')
			nuevoProfesor.save()
			messages.success(request, '¡Profesor modificado correctamente!')
		return redirect ('/listarProfesores/')
	else :
		return redirect('/login/')


def editarProfesor(request,pk):
	"""Muestra la pagina para editar un perfil de profesor"""
	if (request.user.is_authenticated):
		idprofesor = pk
		listaAreas = Area.objects.all()
		profesorRequerido = Profesor.objects.get(pk = pk)
		nombre = profesorRequerido.nombre
		apellido = profesorRequerido.apellido
		titulo = profesorRequerido.titulo
		imgPerfil = profesorRequerido.imgPerfil
		frasePersonal = profesorRequerido.frasePersonal
		descripcion = profesorRequerido.descripcion
		urlLinkedin = profesorRequerido.urlLinkedin
		urlCurriculum = profesorRequerido.urlCurriculum
		estado = profesorRequerido.estado
		context = {
			'nombre':nombre,
			'apellido': apellido,
			'titulo': titulo,
			'imgPerfil': imgPerfil,
			'frasePersonal': frasePersonal,
			'descripcion': descripcion,
			'urlLinkedin': urlLinkedin,
			'urlCurriculum': urlCurriculum,
			'areas': listaAreas,
			'estado': estado,
			'idprofesor': idprofesor
		}
		return render(request, "cenecuAdmin/editarProfesor.html", context)
	else :
		return redirect('/login/')


def eliminarProfesor(request,pk):
	"""Elimina un perfil de profesor de la base de datos"""
	if (request.user.is_authenticated):
		profesor = Profesor.objects.get(pk = pk)
		profesor.delete()
		return redirect('/listarProfesores/')
	else :
		return redirect('/listarProfesores/')
