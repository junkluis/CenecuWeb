#pruebas sin terminar
#faltan configurar los datos para cada prueba

from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class HorarioTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.HorarioHorario = {}
        self.response = self.client.post(reverse('Horario'), 
        	                             self.HorarioData, format = "json")

    def test_crear_Horario(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Horario(self):
        # lista_Horario = Horario.objects.get()
        response = self.client.get( reverse('HorarioEdit',
                                    kwargs={'pk': Horario.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Horario)

    def test_actualizar_Horario(self):
        #Horario = Horario.objects.get()
        nuevo_Horario = { }
        res = self.client.put( reverse('HorarioEdit', kwargs = {'pk': Horario.id } )
                                nuevo_Horario, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Horario(self):
        #Horario = Horario.objects.get()
        res = self.client.delete(reverse('HorarioEdit', kwargs = {'pk': Horario.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class CursoTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.CursoCurso = {}
        self.response = self.client.post(reverse('Curso'), self.CursoData, format = "json")

    def test_crear_Curso(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Curso(self):
        # lista_Curso = Curso.objects.get()
        response = self.client.get( reverse('CursoEdit',
                                    kwargs={'pk': Curso.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Curso)

    def test_actualizar_Curso(self):
        #Curso = Curso.objects.get()
        nuevo_Curso = { }
        res = self.client.put( reverse('CursoEdit', kwargs = {'pk': Curso.id } )
                                nuevo_Curso, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Curso(self):
        #Curso = Curso.objects.get()
        res = self.client.delete(reverse('CursoEdit', kwargs = {'pk': Curso.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class ProfesorTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.ProfesorProfesor = {}
        self.response = self.client.post(reverse('Profesor'), self.ProfesorData, format = "json")

    def test_crear_Profesor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Profesor(self):
        # lista_Profesor = Profesor.objects.get()
        response = self.client.get( reverse('ProfesorEdit',
                                    kwargs={'pk': Profesor.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Profesor)

    def test_actualizar_Profesor(self):
        #Profesor = Profesor.objects.get()
        nuevo_Profesor = { }
        res = self.client.put( reverse('ProfesorEdit', kwargs = {'pk': Profesor.id } )
                                nuevo_Profesor, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Profesor(self):
        #Profesor = Profesor.objects.get()
        res = self.client.delete(reverse('ProfesorEdit', kwargs = {'pk': Profesor.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class CursoProfesorTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.CursoProfesorCursoProfesor = {}
        self.response = self.client.post(reverse('CursoProfesor'),
        	                             self.CursoProfesorData, format = "json")

    def test_crear_CursoProfesor(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_CursoProfesor(self):
        # lista_CursoProfesor = CursoProfesor.objects.get()
        response = self.client.get( reverse('CursoProfesorEdit',
                                    kwargs={'pk': CursoProfesor.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, CursoProfesor)

    def test_actualizar_CursoProfesor(self):
        #CursoProfesor = CursoProfesor.objects.get()
        nuevo_CursoProfesor = { }
        res = self.client.put( reverse('CursoProfesorEdit', kwargs = {'pk': CursoProfesor.id } )
                                nuevo_CursoProfesor, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_CursoProfesor(self):
        #CursoProfesor = CursoProfesor.objects.get()
        res = self.client.delete(reverse('CursoProfesorEdit', kwargs = {'pk': CursoProfesor.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class AreaTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.AreaArea = {}
        self.response = self.client.post(reverse('Area'), self.AreaData, format = "json")

    def test_crear_Area(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Area(self):
        # lista_Area = Area.objects.get()
        response = self.client.get( reverse('AreaEdit',
                                    kwargs={'pk': Area.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Area)

    def test_actualizar_Area(self):
        #Area = Area.objects.get()
        nuevo_Area = { }
        res = self.client.put( reverse('AreaEdit', kwargs = {'pk': Area.id } )
                                nuevo_Area, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Area(self):
        #Area = Area.objects.get()
        res = self.client.delete(reverse('AreaEdit', kwargs = {'pk': Area.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class AnuncioTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.AnuncioAnuncio = {}
        self.response = self.client.post(reverse('Anuncio'), self.AnuncioData, format = "json")

    def test_crear_Anuncio(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Anuncio(self):
        # lista_Anuncio = Anuncio.objects.get()
        response = self.client.get( reverse('AnuncioEdit',
                                    kwargs={'pk': Anuncio.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Anuncio)

    def test_actualizar_Anuncio(self):
        #Anuncio = Anuncio.objects.get()
        nuevo_Anuncio = { }
        res = self.client.put( reverse('AnuncioEdit', kwargs = {'pk': Anuncio.id } )
                                nuevo_Anuncio, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Anuncio(self):
        #Anuncio = Anuncio.objects.get()
        res = self.client.delete(reverse('AnuncioEdit', kwargs = {'pk': Anuncio.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class FraseTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.FraseFrase = {}
        self.response = self.client.post(reverse('Frase'), self.FraseData, format = "json")

    def test_crear_Frase(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Frase(self):
        # lista_Frase = Frase.objects.get()
        response = self.client.get( reverse('FraseEdit',
                                    kwargs={'pk': Frase.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Frase)

    def test_actualizar_Frase(self):
        #Frase = Frase.objects.get()
        nuevo_Frase = { }
        res = self.client.put( reverse('FraseEdit', kwargs = {'pk': Frase.id } )
                                nuevo_Frase, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Frase(self):
        #Frase = Frase.objects.get()
        res = self.client.delete(reverse('FraseEdit', kwargs = {'pk': Frase.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class GoalsListTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.GoalsListGoalsList = {}
        self.response = self.client.post(reverse('GoalsList'), self.GoalsListData, format = "json")

    def test_crear_GoalsList(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_GoalsList(self):
        # lista_GoalsList = GoalsList.objects.get()
        response = self.client.get( reverse('GoalsListEdit',
                                    kwargs={'pk': GoalsList.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, GoalsList)

    def test_actualizar_GoalsList(self):
        #GoalsList = GoalsList.objects.get()
        nuevo_GoalsList = { }
        res = self.client.put( reverse('GoalsListEdit', kwargs = {'pk': GoalsList.id } )
                                nuevo_GoalsList, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_GoalsList(self):
        #GoalsList = GoalsList.objects.get()
        res = self.client.delete(reverse('GoalsListEdit', kwargs = {'pk': GoalsList.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class AreaInteresTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.AreaInteresAreaInteres = {}
        self.response = self.client.post(reverse('AreaInteres'), self.AreaInteresData, format = "json")

    def test_crear_AreaInteres(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_AreaInteres(self):
        # lista_AreaInteres = AreaInteres.objects.get()
        response = self.client.get( reverse('AreaInteresEdit',
                                    kwargs={'pk': AreaInteres.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, AreaInteres)

    def test_actualizar_AreaInteres(self):
        #AreaInteres = AreaInteres.objects.get()
        nuevo_AreaInteres = { }
        res = self.client.put( reverse('AreaInteresEdit', kwargs = {'pk': AreaInteres.id } )
                                nuevo_AreaInteres, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_AreaInteres(self):
        #AreaInteres = AreaInteres.objects.get()
        res = self.client.delete(reverse('AreaInteresEdit', kwargs = {'pk': AreaInteres.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class UsuarioRolTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.UsuarioRolUsuarioRol = {}
        self.response = self.client.post(reverse('UsuarioRol'), self.UsuarioRolData, format = "json")

    def test_crear_UsuarioRol(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_UsuarioRol(self):
        # lista_UsuarioRol = UsuarioRol.objects.get()
        response = self.client.get( reverse('UsuarioRolEdit',
                                    kwargs={'pk': UsuarioRol.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, UsuarioRol)

    def test_actualizar_UsuarioRol(self):
        #UsuarioRol = UsuarioRol.objects.get()
        nuevo_UsuarioRol = { }
        res = self.client.put( reverse('UsuarioRolEdit', kwargs = {'pk': UsuarioRol.id } )
                                nuevo_UsuarioRol, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_UsuarioRol(self):
        #UsuarioRol = UsuarioRol.objects.get()
        res = self.client.delete(reverse('UsuarioRolEdit', kwargs = {'pk': UsuarioRol.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class NotaTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.NotaNota = {}
        self.response = self.client.post(reverse('Nota'), self.NotaData, format = "json")

    def test_crear_Nota(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Nota(self):
        # lista_Nota = Nota.objects.get()
        response = self.client.get( reverse('NotaEdit',
                                    kwargs={'pk': Nota.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Nota)

    def test_actualizar_Nota(self):
        #Nota = Nota.objects.get()
        nuevo_Nota = { }
        res = self.client.put( reverse('NotaEdit', kwargs = {'pk': Nota.id } )
                                nuevo_Nota, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Nota(self):
        #Nota = Nota.objects.get()
        res = self.client.delete(reverse('NotaEdit', kwargs = {'pk': Nota.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class ContenidoCompartidoTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.ContenidoCompartidoContenidoCompartido = {}
        self.response = self.client.post(reverse('ContenidoCompartido'), self.ContenidoCompartidoData, format = "json")

    def test_crear_ContenidoCompartido(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_ContenidoCompartido(self):
        # lista_ContenidoCompartido = ContenidoCompartido.objects.get()
        response = self.client.get( reverse('ContenidoCompartidoEdit',
                                    kwargs={'pk': ContenidoCompartido.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, ContenidoCompartido)

    def test_actualizar_ContenidoCompartido(self):
        #ContenidoCompartido = ContenidoCompartido.objects.get()
        nuevo_ContenidoCompartido = { }
        res = self.client.put( reverse('ContenidoCompartidoEdit', kwargs = {'pk': ContenidoCompartido.id } )
                                nuevo_ContenidoCompartido, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_ContenidoCompartido(self):
        #ContenidoCompartido = ContenidoCompartido.objects.get()
        res = self.client.delete(reverse('ContenidoCompartidoEdit', kwargs = {'pk': ContenidoCompartido.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class RegistroUsuarioCursoTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.RegistroUsuarioCursoRegistroUsuarioCurso = {}
        self.response = self.client.post(reverse('RegistroUsuarioCurso'), self.RegistroUsuarioCursoData, format = "json")

    def test_crear_RegistroUsuarioCurso(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_RegistroUsuarioCurso(self):
        # lista_RegistroUsuarioCurso = RegistroUsuarioCurso.objects.get()
        response = self.client.get( reverse('RegistroUsuarioCursoEdit',
                                    kwargs={'pk': RegistroUsuarioCurso.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, RegistroUsuarioCurso)

    def test_actualizar_RegistroUsuarioCurso(self):
        #RegistroUsuarioCurso = RegistroUsuarioCurso.objects.get()
        nuevo_RegistroUsuarioCurso = { }
        res = self.client.put( reverse('RegistroUsuarioCursoEdit', kwargs = {'pk': RegistroUsuarioCurso.id } )
                                nuevo_RegistroUsuarioCurso, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_RegistroUsuarioCurso(self):
        #RegistroUsuarioCurso = RegistroUsuarioCurso.objects.get()
        res = self.client.delete(reverse('RegistroUsuarioCursoEdit', kwargs = {'pk': RegistroUsuarioCurso.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



class TelefonosTestCase(TestCase):
    
    def set_up(self):
        self.client = APIClient()
        self.TelefonosTelefonos = {}
        self.response = self.client.post(reverse('Telefonos'), self.TelefonosData, format = "json")

    def test_crear_Telefonos(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_obtener_un_Telefonos(self):
        # lista_Telefonos = Telefonos.objects.get()
        response = self.client.get( reverse('TelefonosEdit',
                                    kwargs={'pk': Telefonos.id }), format = "json")
        self.assertEqual(response.status_code, status.HTTP_200_ok)
        self.assertContains(response, Telefonos)

    def test_actualizar_Telefonos(self):
        #Telefonos = Telefonos.objects.get()
        nuevo_Telefonos = { }
        res = self.client.put( reverse('TelefonosEdit', kwargs = {'pk': Telefonos.id } )
                                nuevo_Telefonos, format="json")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_eliminar_Telefonos(self):
        #Telefonos = Telefonos.objects.get()
        res = self.client.delete(reverse('TelefonosEdit', kwargs = {'pk': Telefonos.id}),
                                  format="json", follow=True)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)






'''
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
'''