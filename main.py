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

grupo1 = Grupo()
grupo2 = Grupo("Grupo 32")
grupo3 = Grupo("Grupo 23", [asignatura1])
grupo4 = Grupo("Grupo 12", [asignatura1, asignatura2], ["Jaime", "David", "Oswaldo"])

grupo1.agregarAlumno("Alumno10")
grupo2.agregarAlumno("Alumno20")
grupo3.agregarAlumno("Alumno30")
grupo4.agregarAlumno("Alumno40")

grupo1.agregarAlumno("Alumno11")
grupo2.agregarAlumno("Alumno21")
grupo3.agregarAlumno("Alumno31")
grupo4.agregarAlumno("Alumno41")

grupo1.agregarAlumno("Alumno14", ["Alumno12", "Alumno13"])
grupo2.agregarAlumno("Alumno24", ["Alumno22", "Alumno23"])
grupo3.agregarAlumno("Alumno34", ["Alumno32", "Alumno33"])
grupo4.agregarAlumno("Alumno44", ["Alumno42", "Alumno43"])

ok = False
if str(grupo1) == "Grupo de estudiantes: grupo predeterminado" and grupo1.listadoAlumnos == ["Alumno10", "Alumno11", "Alumno12", "Alumno13", "Alumno14"] and\
    str(grupo2) == "Grupo de estudiantes: Grupo 32" and grupo2.listadoAlumnos == ["Alumno20", "Alumno21", "Alumno22", "Alumno23", "Alumno24"] and \
    str(grupo3) == "Grupo de estudiantes: Grupo 23" and grupo3.listadoAlumnos == ["Alumno30", "Alumno31", "Alumno32", "Alumno33", "Alumno34"] and\
    str(grupo4) == "Grupo de estudiantes: Grupo 12" and grupo4.listadoAlumnos == ["Jaime", "David", "Oswaldo", "Alumno40", "Alumno41", "Alumno42", "Alumno43", "Alumno44"]:
    ok = True
print((grupo1.listadoAlumnos))
print((grupo2.listadoAlumnos))
print((grupo3.listadoAlumnos))
print((grupo4.listadoAlumnos))
print(ok)