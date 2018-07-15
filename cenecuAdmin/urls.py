# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.contrib.auth.views import login
from django.conf.urls.static import static

urlpatterns = [
	url(r'^adminIndex/$', views.index , name = 'index'),
	url(r'^login/$', views.iniciarSesion, name='iniciarSesion'),
	url(r'^nuevoCurso/$',views.nuevoCurso, name='nuevoCurso' ),
	url(r'^crearCurso/$',views.crearCurso,name='crearCurso'),
	url(r'^editarCurso/(?P<pk>[0-9]+)', views.editarCurso, name='editarCurso'),
	url(r'^modificarCurso/$',views.modificarCurso,name='modificarCurso'),
	url(r'^eliminarCurso/(?P<pk>[0-9]+)$', views.eliminarCurso, name='eliminarCurso'),
	url(r'^listarProfesores/$', views.listarProfesores , name = 'listarProfesores'),
	url(r'^nuevoProfesor/$',views.nuevoProfesor, name='nuevoProfesor'),
	url(r'^crearProfesor/$',views.crearProfesor, name='crearProfesor' ),
	url(r'^editarProfesor/(?P<pk>[0-9]+)', views.editarProfesor, name='editarProfesor'),
	url(r'^modificarProfesor/$',views.modificarProfesor,name='modificarProfesor'),
	url(r'^eliminarProfesor/(?P<pk>[0-9]+)$', views.eliminarProfesor, name='eliminarProfesor'),
	url(r'^logout/$',views.cerrarSesion, name='cerrarSesion'),
]




