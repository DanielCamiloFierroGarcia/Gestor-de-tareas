from utilidades import pedir_entero, cargar_tareas

from tareas import (
    ver_tareas,
    agregar_tareas,
    completar_tarea, 
    eliminar_tarea,
    editar_tarea
)

tareas = cargar_tareas()


def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Editar tarea")
    print("6. Salir")     


while True:
    mostrar_menu()
    opcion = pedir_entero("Elige una opcion (1-6): ")
    if opcion == 1:
        ver_tareas(tareas)
    elif opcion == 2:
        agregar_tareas(tareas)
    elif opcion == 3:
        completar_tarea(tareas)
    elif opcion == 4:
        eliminar_tarea(tareas)
    elif opcion == 5:
        editar_tarea(tareas)
    elif opcion == 6:
        print("Chao")
        break
    else:
        print("Opcion no valida")