#Archivo MAIN

from utilidades import pedir_entero, cargar_tareas, mostrar_menu
from clases.modelo_tarea import Tarea
from clases.tareas_con_fecha import TareaConFecha

from tareas import (
    ver_tareas,
    agregar_tareas,
    completar_tarea,
    eliminar_tarea,
    editar_tarea,
    descargar_backups_desde_s3, 
    agregar_tarea_con_fecha
)

tareas = cargar_tareas()
  
while True:
    mostrar_menu()
    opcion = pedir_entero("Elige una opcion (1-8): ")
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
        descargar_backups_desde_s3()
    elif opcion == 7:
        agregar_tarea_con_fecha(tareas)
    elif opcion == 8:
        print("Chao")
        break
    else:
        print("Opcion no valida")