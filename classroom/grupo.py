from classroom.asignatura import Asignatura

class Grupo:
    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[],estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x , y in kwargs.items():
            self._asignaturas.append(Asignatura(y))

    def agregarAlumno(self, *alumno, lista=None):
        lista=list(alumno)
        for i in lista:
            if isinstance(i, list):
                lista.remove(i)
                lista.extend(i)
        lista=lista[1:]+[lista[0]]
        self.listadoAlumnos = self.listadoAlumnos + lista

        

    def __str__(self):
        return ('Grupo de estudiantes:'+' '+self._grupo)

   # @ classmethod
    #def asignarNombre(cls, nombre="Grado 10"):
    #    cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

   # @ classmethod
   # def asignarNombre(cls, nombre="Grado 4"):
    #    cls.grado = nombre
