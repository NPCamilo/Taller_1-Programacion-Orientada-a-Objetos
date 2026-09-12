"""
Escribir un programa que almacene las asignaturas de un curso
en una lista, pida al usuario las 4 notas de cada materia y en
pantalla mostrar el promedio que ha sacado en cada materia y si
alguna materia queda por debajo de la nota 3 debe salir en
pantalla “asignatura perdida”, luego se deben calcular el
promedio general de todas las materias si el promedio está por
debajo de 3 debe imprimir “semestre perdido”, si esta entre 3 y 4
debe imprimir “buen trabajo”, si el promedio esta entre 4 y 5
debe imprimir “felicidades serás becado”.
Salida de datos:
Matemáticas : nota1: 2, nota2: 2, nota3: 2, nota 4: 2
Promedio de matemáticas: 2 : asignatura perdida
Inglés : nota1: 3, nota2: 3, nota3: 3, nota 4: 3
Promedio de matemáticas: 3 : asignatura ganada
Promedio general: 2.5 : “Semestre perdido”

"""

#Bloque para cálculo de promedios de asignatura individuales
for asignatura in range(3):
    Asignaturas = input("Ingrese el nombre de la asignatura: ")
    Notas = []
    for calificacion in range(4):
        nota = float(input(f"Ingrese la nota {calificacion + 1} de {Asignaturas}: "))
        Notas.append(nota)
    Promedio = []
    Contador_Asignaturas = 0
    Promedio.append(sum(Notas) / len(Notas))
    if Promedio[Contador_Asignaturas] < 3:
        print(f"\nPromedio de {Asignaturas}: {Promedio[Contador_Asignaturas]} : asignatura perdida\n")
    else:
        print(f"\nPromedio de {Asignaturas}: {Promedio[Contador_Asignaturas]} : asignatura ganada\n")
    Contador_Asignaturas += 1

#Bloque para cálculo de promedio general y evaluación del semestre
if sum(Promedio) / len(Promedio) < 3:
    print(f"\n\nPromedio general: {sum(Promedio) / len(Promedio)} : Semestre perdido\n")
elif sum(Promedio) / len(Promedio) < 4:
    print(f"\n\nPromedio general: {sum(Promedio) / len(Promedio)} : Buen trabajo\n")
else:
    print(f"\n\nPromedio general: {sum(Promedio) / len(Promedio)} : Felicidades serás becado\n")