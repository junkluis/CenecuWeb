from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {

	url( r'^Curso/$' , CursoView.as_view(), name="Curso"),
	url( r'^CursoProfesor/$' , CursoProfesorView.as_view(), name="CursoProfesor"),
	url( r'^Profesor/$' , ProfesorView.as_view(), name="Profesor"),
	url( r'^Area/$' , AreaView.as_view(), name="Area"),
	url( r'^AreaInteres/$' , AreaInteresView.as_view(), name="AreaInteres"),
	url( r'^UsuarioRol/$' , UsuarioRolView.as_view(), name="UsuarioRol"),
	url( r'^Nota/$' , NotaView.as_view(), name="Nota"),
	url( r'^GoalsList/$' , GoalsListView.as_view(), name="GoalsList"),
	url( r'^Frase/$' , FraseView.as_view(), name="Frase"),
	url( r'^Anuncio/$' , AnuncioView.as_view(), name="Anuncio"),
	url( r'^BolsaDeTrabajo/$' , BolsaDeTrabajoView.as_view(), name="BolsaDeTrabajo"),
	url( r'^UsuariosTrabajo/$' , UsuariosTrabajoView.as_view(), name="UsuariosTrabajo"),

	url( r'^Curso/(?P<pk>[0-9]+)/$' , CursoEdit.as_view(), name="CursoEdit"),
	url( r'^CursoProfesor/(?P<pk>[0-9]+)/$' , CursoProfesorEdit.as_view(), name="CursoProfesorEdit"),
	url( r'^Profesor/(?P<pk>[0-9]+)/$' , ProfesorEdit.as_view(), name="ProfesorEdit"),
	url( r'^Area/(?P<pk>[0-9]+)/$' , AreaEdit.as_view(), name="AreaEdit"),
	url( r'^AreaInteres/(?P<pk>[0-9]+)/$' , AreaInteresEdit.as_view(), name="AreaInteresEdit"),
	url( r'^UsuarioRol/(?P<pk>[0-9]+)/$' , UsuarioRolEdit.as_view(), name="UsuarioRolEdit"),
	url( r'^Nota/(?P<pk>[0-9]+)/$' , NotaEdit.as_view(), name="NotaEdit"),
	url( r'^GoalsList/(?P<pk>[0-9]+)/$' , GoalsListEdit.as_view(), name="GoalsListEdit"),
	url( r'^Frase/(?P<pk>[0-9]+)/$' , FraseEdit.as_view(), name="FraseEdit"),
	url( r'^Anuncio/(?P<pk>[0-9]+)/$' , AnuncioEdit.as_view(), name="AnuncioEdit"),
	url( r'^BolsaDeTrabajo/(?P<pk>[0-9]+)/$' , BolsaDeTrabajoEdit.as_view(), name="BolsaDeTrabajoEdit"),
	url( r'^UsuariosTrabajo/(?P<pk>[0-9]+)/$' , UsuariosTrabajoEdit.as_view(), name="UsuariosTrabajoEdit"),

	url( r'^Hello/$', hello_world, name="testOverride"),
	url( r'^loginCenecu/$', loginCenecu, name="login"),
	url( r'^notasUser/(?P<pk>[0-9]+)/$' , notasPorUser, name="NotasPorUsuario"),
	url( r'^borrarNota/(?P<pk>[0-9]+)/$' , borrarNota, name="borrarNota"),
	url( r'^registrarUsuario/$' , registrarUsuario, name="registrarUsuario"),
	url( r'^logOut/$' , logOut, name="logOut"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
