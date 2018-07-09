# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse



class AreaTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()
		self.areaData = { 'nombre' : 'Area de prueba',
							'descripcion' : 'Hello my dark friend',
							'imgArea' : 'http://satgeo.com/wp-content/uploads/2014/03/img.gif',
							'estado' : 'Activo' }
		self.response = self.client.post(reverse('Area'),
											self.areaData,
											format = "json")

	def testCrearArea(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def testObtenerUnaArea(self):
		area = Area.objects.get()
		response = self.client.get(
				reverse('AreaEdit',
				kwargs={'pk' : area.id } ), format = "json" )
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, area)


	def testActualizarArea(self):
		area = Area.objects.get()
		nuevaArea = { 'nombre' : 'Area de prueba',
						'descripcion' : 'Hello my dark friend',
						'imgArea' : 'http://satgeo.com/wp-content/uploads/2014/03/img.gif',
						'estado' : 'Inactiva' }
		res = self.client.put(
			reverse('AreaEdit', kwargs = {'pk': area.id}),
					nuevaArea, format = 'json'
			)
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def testEliminarArea(self):
		area = Area.objects.get()
		res = self.client.delete(
			reverse('AreaEdit', kwargs = {'pk': area.id}),
					 format = 'json', follow=True)
		self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)


class CursoTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()
		self.cursoData = { 'nombre' : 'Curso de Prueba',
							'descripcion' : 'Este es un curso de prueba',
							'urlPensum' : 'https://s1.q4cdn.com/806093406/files/doc_downloads/test.pdf',
							'duracion' : '10',
							'costo' : '50.5',
							'imgCurso' : 'http://www.consultoraponcio.com/wp-content/uploads/2016/04/test.png',
							'horario' : '13:30-15:30',
							'estado' : 'Activo' }
		self.response = self.client.post(reverse('Curso'),
											self.cursoData,
											format = "json")

	def testCrearCurso(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def testObtenerUnCurso(self):
		curso = Curso.objects.get()
		response = self.client.get(
				reverse('CursoEdit',
				kwargs={'pk' : curso.id } ), format = "json" )
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, curso)

	def testActualizarCurso(self):
		curso = Curso.objects.get()
		nuevoCurso = { 'nombre' : 'Curso de Prueba editado',
						'descripcion' : '¿QUÉ LE DECIMOS AL DIOS DE LA MUERTE? HOY NO',
						'urlPensum' : 'https://s1.q4cdn.com/806093406/files/doc_downloads/test.pdf',
						'duracion' : '50',
						'costo' : '150.5',
						'imgCurso' : 'http://www.consultoraponcio.com/wp-content/uploads/2016/04/test.png',
						'horario' : '13:30-15:30',
						'estado' : 'Activo' }
		res = self.client.put(
			reverse('CursoEdit', kwargs = {'pk': curso.id}),
					nuevoCurso, format = 'json'
			)
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def testEliminaCurso(self):
		curso = Curso.objects.get()
		res = self.client.delete(
			reverse('CursoEdit', kwargs = {'pk': curso.id}),
					 format = 'json', follow=True)
		self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)


class NotasTestCase(TestCase):
	
	def setUp(self):
		user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
		self.client = APIClient()
		self.notaData = { "titulo": "dfghj",
							"descripion": "dfghj",
							"fechaLimite": "2018-06-08",
							"notificacion": "true",
							"icono": "luis.jpg",
							"usuarioId": "1"}
		self.response = self.client.post(reverse('Nota'), 
											self.notaData,
											format = "json" )

	def testCrearNota(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def testObtenerUnaNota(self):
		nota = Nota.objects.get()
		response = self.client.get(
				reverse('NotaEdit',
				kwargs={'pk' : nota.id } ), format = "json" )
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, nota)

	def testActualizarNota(self):
		nota = Nota.objects.get()
		nuevaNota = { 'titulo' : 'Un león',
						'descripion' : 'Un león no se preocupa por las opiniones de las ovejas.',
						'fechaLimite' : '2018-06-08',
						'notificacion' : 'false',
						'icono' : 'assets/imgs/goal.png',
						'usuarioId' : '1' }
		res = self.client.put(
			reverse('NotaEdit', kwargs = {'pk': nota.id}),
					nuevaNota, format = 'json'
			)
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def testEliminaNota(self):
		nota = Nota.objects.get()
		res = self.client.delete(
			reverse('NotaEdit', kwargs = {'pk': nota.id}),
					 format = 'json', follow=True)
		self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)

	def testNotasPorUser(self):

		res = self.client.get( reverse('NotasPorUsuario', kwargs = {'pk': '1'}),
					 					format = 'json', follow=True)
		self.assertEqual(res.status_code, status.HTTP_200_OK)


class ProfesorTestCase(TestCase):
	
	def setUp(self):
		area = Area(nombre="testArea", descripcion="testArea", imgArea="testImg", estado="activa")
		area.save()

		self.client = APIClient()
		self.profesorData = {"nombre": "Narcisa",
								"apellido": "Colcha",
								"titulo": "Ing. Computación",
								"imgPerfil": "http://127.0.0.1:8000/static/images/perfil1.jpg",
								"frasePersonal": "Today is Life",
								"descripcion": "Como ingeniero, mi formación académica, humana y laboral se ha enfocado al desarrollo y la implementación de propuestas útiles en el campo de la productividad. Soy un profesional comprometido con la investigación, el liderazgo y el trabajo en equipo.",
								"areaEspecializacion": "1",
								"urlLinkedin": "www.linkedin.com",
								"urlCurriculum": "http://127.0.0.1:8000/static/cv/cv1.pdf",
								"estado": "Activo"
						    }
		self.response = self.client.post(reverse('Profesor'), 
											self.profesorData,
											format = "json" )


	def testCrearProfesor(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def testObtenerUnProfesor(self):
		profe = Profesor.objects.get()
		response = self.client.get(
				reverse('ProfesorEdit',
				kwargs={'pk' : profe.id } ), format = "json" )
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, profe)

	def testActualizarProfesor(self):
		profe = Profesor.objects.get()
		nuevoInfo = {"nombre":"Ned",
						"apellido":"Stark",
						"titulo":"Lord de Invernalia",
						"imgPerfil":"https://vignette.wikia.nocookie.net/hieloyfuego/images/8/8c/Eddard_Stark_by_Elia_Mervi%C2%A9.jpg/revision/latest/scale-to-width-down/347?cb=20131124004256",
						"frasePersonal":"El invierno se acerca",
						"descripcion":" Su barba empezaba a tornarse grisácea en su último año de vida.[1] De acuerdo a Lady Catelyn, no es ni tan alto ni tan atractivo como lo fue su hermano mayor, Brandon Stark",
						"areaEspecializacion":"1",
						"urlLinkedin":"http://hieloyfuego.wikia.com/wiki/Eddard_Stark",
						"urlCurriculum":"http://hieloyfuego.wikia.com/wiki/Eddard_Stark",
						"estado":"Muerto" }
		res = self.client.put(
			reverse('ProfesorEdit', kwargs = {'pk': profe.id}),
					nuevoInfo, format = 'json'
			)
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def testEliminarProfesor(self):
		profe = Profesor.objects.get()
		res = self.client.delete(
			reverse('ProfesorEdit', kwargs = {'pk': profe.id}),
					 format = 'json', follow=True)
		self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)


class UserTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()
		user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='Glass onion123')
		rol = UsuarioRol(usuarioId = user, rol="test" )
		rol.save()

	def testLogIn(self):
		userData = { "username":"john", "password":"Glass onion123"  }
		res = self.client.post(reverse('login'), userData, format = 'json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def testLogOut(self):
		res = self.client.get(reverse('logOut') , format = 'json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def testRegistrarUser(self):
		newUser = {"user":"YugiMoto",
					"pass":"Mago Oscuro123",
					"apellido":"Yugi",
					"nombre":"Moto",
					"email":"yugi@gmail.com"}

		response = self.client.post(reverse('registrarUsuario'), 
											newUser,
											format = "json" )
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		

class UsuarioRolsTestCase(TestCase):
	pass


class AreaInteresTestCase(TestCase):
	pass


class AnunciosTestCase(TestCase):
	pass


class BolsaDeTrabajosTestCase(TestCase):
	pass


class CursoProfesorsTestCase(TestCase):
	pass


class FrasesTestCase(TestCase):
	pass


class GoalsListsTestCase(TestCase):
	pass


class UsuariosTrabajosTestCase(TestCase):
	pass
