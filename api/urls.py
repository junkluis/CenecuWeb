#!CenecuWeb/api/urls.py
"""Rutas del API"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HorarioView, CursoView, ProfesorView, CursoProfesorView
from .views import AreaView, AnuncioView, FraseView, GoalsListView
from .views import AreaInteresView, UsuarioRolView, NotaView, TelefonosEdit
from .views import ContenidoCompartidoView, RegistroUsuarioCursoView

from .views import TelefonosView, HorarioEdit, CursoEdit, ProfesorEdit
from .views import CursoProfesorEdit, AreaEdit, AnuncioEdit, FraseEdit
from .views import GoalsListEdit, AreaInteresEdit, UsuarioRolEdit
from .views import NotaEdit, ContenidoCompartidoEdit, RegistroUsuarioCursoEdit
from . import views


urlpatterns = {
    url(r'^$', views.apiIndex, name="Index"),
    url(r'^Horario/$', HorarioView.as_view(), name="Horario"),
    url(r'^Curso/$', CursoView.as_view(), name="Curso"),
    url(r'^Profesor/$', ProfesorView.as_view(), name="Profesor"),
    url(r'^Curso_profesor/$', CursoProfesorView.as_view(),
        name="Curso_profesor"),
    url(r'^Area/$', AreaView.as_view(), name="Area"),
    url(r'^Anuncio/$', AnuncioView.as_view(), name="Anuncio"),
    url(r'^Frase/$', FraseView.as_view(), name="Frase"),
    url(r'^Goals_list/$', GoalsListView.as_view(), name="Goals_list"),
    url(r'^Area_interes/$', AreaInteresView.as_view(), name="Area_interes"),
    url(r'^Usuario_rol/$', UsuarioRolView.as_view(), name="Usuario_rol"),
    url(r'^Nota/$', NotaView.as_view(), name="Nota"),
    url(r'^Contenido_compartido/$', ContenidoCompartidoView.as_view(),
        name="Contenido_compartido"),
    url(r'^Registro_usuario_curso/$', RegistroUsuarioCursoView.as_view(),
        name="Registro_usuario_curso"),
    url(r'^telefonos/$', TelefonosView.as_view(), name="telefonos"),

    url(r'^Horario/(?P<pk>[0-9]+)/$', HorarioEdit.as_view(),
        name="HorarioEdit"),
    url(r'^Curso/(?P<pk>[0-9]+)/$', CursoEdit.as_view(),
        name="CursoEdit"),
    url(r'^Profesor/(?P<pk>[0-9]+)/$', ProfesorEdit.as_view(),
        name="ProfesorEdit"),
    url(r'^Curso_profesor/(?P<pk>[0-9]+)/$', CursoProfesorEdit.as_view(),
        name="Curso_profesorEdit"),
    url(r'^Area/(?P<pk>[0-9]+)/$', AreaEdit.as_view(), name="AreaEdit"),
    url(r'^Anuncio/(?P<pk>[0-9]+)/$', AnuncioEdit.as_view(),
        name="AnuncioEdit"),
    url(r'^Frase/(?P<pk>[0-9]+)/$', FraseEdit.as_view(), name="FraseEdit"),
    url(r'^Goals_list/(?P<pk>[0-9]+)/$', GoalsListEdit.as_view(),
        name="Goals_listEdit"),
    url(r'^Area_interes/(?P<pk>[0-9]+)/$', AreaInteresEdit.as_view(),
        name="Area_interesEdit"),
    url(r'^Usuario_rol/(?P<pk>[0-9]+)/$', UsuarioRolEdit.as_view(),
        name="Usuario_rolEdit"),
    url(r'^Nota/(?P<pk>[0-9]+)/$', NotaEdit.as_view(), name="NotaEdit"),
    url(r'^Contenido_compartido/(?P<pk>[0-9]+)/$',
        ContenidoCompartidoEdit.as_view(), name="Contenido_compartidoEdit"),
    url(r'^Registro_usuario_curso/(?P<pk>[0-9]+)/$',
        RegistroUsuarioCursoEdit.as_view(), name="Registro_usuario_cursoEdit"),
    url(r'^telefonos/(?P<pk>[0-9]+)/$', TelefonosEdit.as_view(),
        name="telefonosEdit"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
