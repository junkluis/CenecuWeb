# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^adminIndex/$', views.index , name = 'index'),
	url(r'^eliminarCurso/(?P<pk>[0-9]+)$', views.eliminarCurso, name='eliminarCurso'),
	url(r'^login$', views.iniciarSesion, name='iniciarSesion'),
	url(r'^editarCurso/(?P<pk>[0-9]+)', views.editarCurso, name='editarCurso'),
	url(r'^nuevoCurso/$',views.nuevoCurso, name='nuevoCurso' ),

]




