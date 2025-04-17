# Aplicación para administrar tareas personales, con funciones para agregar, completar y priorizar tareas.

# Requisitos:

#     Agregar tarea solicitando:

#         Descripción (no vacía).

#         Prioridad (Alta, Media, Baja).

#         Fecha límite (formato dd/mm/aaaa).

#     Marcar tarea como completada.

#     Eliminar tarea por descripción.

#     Mostrar tareas ordenadas por prioridad y fecha.

#     Generar un reporte con:

#         Total de tareas pendientes/completadas.

#         Tarea más urgente (prioridad Alta y fecha próxima).

#     Menú interactivo con validaciones (ej.: fecha incorrecta).

#     Usar listas de diccionarios para almacenar tareas.

car_tareas = []

def menu_prioridad():
    print("---OPCIONES A ELEGIR---")
    print("1.Alta")
    print("2.Media")
    print("3.Baja")
def agregar_tarea():
    tareas = {}
    descripcion : str = str(input("Dame la descripcion de la tarea: ")).capitalize()
    tareas["Tarea"] = descripcion

    menu_prioridad()
    prioridad = int(input("DAME UNA OPCION: "))
    if prioridad == 1:
        prioridad = "Alta"
        tareas["Prioridad"] = prioridad
    elif prioridad == 2:
        prioridad = "Media"
        tareas["Prioridad"] = prioridad
    elif prioridad == 3:
        prioridad = "Baja"
        tareas["Prioridad"] = prioridad
    else:
        print("✖️OPCION NO VALIDA✖️")
    
    fecha =  str(input("DAME LA FECHA LIMITE: "))
    tareas["Fecha"] = fecha
    car_tareas.append(tareas)
    print("LA TAREA FUE AGREGADA CORRECTAMENTE✅")


def mostrar_todos_las_tareas():
    for tarea in car_tareas:
        print(tarea)

def marcar_tarea_completada():
    pass

def eliminar_tarea():
    tarea_a_eliminar = str(input("DAME LA DESCRIPCION DE LA TAREA: "))
    for tarea in car_tareas:
        if tarea["Tarea"] == tarea_a_eliminar:
            tarea.remove
            print("TAREA ELIMINADA✅")

def repote():
    total = len(car_tareas)
    print(total)
def menu():
    pass


while True:
    opcion = int(input("DAME UNA OPCION: "))
    menu()
    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        mostrar_todos_las_tareas()
    elif opcion == 3:
        eliminar_tarea()
    elif opcion == 4:
        repote()
    elif opcion == 5:
        break
    


    
