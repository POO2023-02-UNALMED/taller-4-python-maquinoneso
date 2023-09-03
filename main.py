from classroom.asignatura import Asignatura
from classroom.grupo import Grupo

if __name__ == "__main__":
    asignatura1 = Asignatura("Matematicas")
    asignatura2 = Asignatura("Castellano", "Salon 201")
    grupo1 = Grupo()

    print(asignatura1)
    print(grupo1)
    print(grupo1.grado)

    grupo2 = Grupo("Grupo 5", [], ["Alejandro", "Carlos"])

    grupo3 = Grupo()
    grupo4 = Grupo()
    grupo5 = Grupo()
    grupo3.agregarAlumno("Kelly")
    grupo4.agregarAlumno("Santiago", ["Jaime", "Pedro"])
    grupo5.agregarAlumno("Javier")

    print(grupo3.listadoAlumnos)
    print(grupo4.listadoAlumnos)
    print(grupo5.listadoAlumnos)

    grupo3.listadoAsignaturas(as1="Ciencias", as2="Quimica", as3="Ingles")
    print(len(grupo3._asignaturas))

    Grupo.asignarNombre("Grado 1")
    print(Grupo.grado)
    Grupo.asignarNombre()
    print(Grupo.grado)




asignatura1 = Asignatura("Vision por Computador")
asignatura2 = Asignatura("POO", "Salon 503B")

grupo = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])
grupo.listadoAsignaturas(asignatura1="Fundamentos de programacion",
                        asignatura2="Ecuaciones diferenciales",
                        asignatura3="Inteligencia artificial")

ok = False
if grupo._asignaturas[0]._nombre == "Vision por Computador" and\
    grupo._asignaturas[1]._nombre == "POO" and\
    grupo._asignaturas[2]._nombre == "Fundamentos de programacion" and\
    grupo._asignaturas[3]._nombre == "Ecuaciones diferenciales" and\
    grupo._asignaturas[4]._nombre == "Inteligencia artificial":
    ok = True

print(ok)
print(grupo._asignaturas[0]._nombre)
print(grupo._asignaturas[1]._nombre)
print(grupo._asignaturas[2]._nombre)
print(grupo._asignaturas[3]._nombre)
print(grupo._asignaturas[4]._nombre)
