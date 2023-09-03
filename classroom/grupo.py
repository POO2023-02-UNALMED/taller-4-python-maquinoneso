from classroom.asignatura import Asignatura

class Grupo:
    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[],estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs:
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, *alumno, lista=None):
        lista=list(alumno)
        for i in lista:
            if isinstance(i, list):
                lista.remove(i)
                lista.extend(i)
        self.listadoAlumnos = self.listadoAlumnos + lista

        

    def __str__(self):
        return ('Grupo de estudiuantes:'+' '+self._grupo)

   # @ classmethod
    #def asignarNombre(cls, nombre="Grado 10"):
    #    cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

   # @ classmethod
   # def asignarNombre(cls, nombre="Grado 4"):
    #    cls.grado = nombre
