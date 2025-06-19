#Archivo MAIN

from utils.utilidades import pedir_entero, cargar_tareas, mostrar_menu, editar_fecha_limite, opciones_ver_tareas
from clases.modelo_tarea import Tarea
from clases.tareas_con_fecha import TareaConFecha

from tareas import (
    agregar_tareas,
    completar_tarea,
    eliminar_tarea,
    editar_tarea,
    descargar_backups_desde_s3, 
    agregar_tarea_con_fecha, 
    mostrar_tareas_filtradas
)

tareas = cargar_tareas()
  
while True:
    mostrar_menu()
    opcion = pedir_entero("Elige una opcion (1-9): ")
    if opcion == 1:
        while True:
            opciones_ver_tareas()
            opcion2 = pedir_entero("Elige una opcion (1-4): ")
            if opcion2 == 1:
                mostrar_tareas_filtradas(tareas,)
                break
            elif opcion2 == 2:
                mostrar_tareas_filtradas(tareas, True)
                break
            elif opcion2 == 3:
                mostrar_tareas_filtradas(tareas, False)
                break
            elif opcion2 == 4:
                break
            else:
                print("Opcion no valida")
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
        editar_fecha_limite(tareas)
    elif opcion == 9:
        print("Chao")
        break
    else:
        print("Opcion no valida")