import json
import os
from s3_utils import subir_backup, descargar_backup
from clases.modelo_tarea import Tarea
from clases.tareas_con_fecha import TareaConFecha

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Ver tareas")
    print("2. Agregar tarea") 
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Editar tarea")
    print("6. Restaurar tareas desde backup")
    print("7. Agregar tarea con fecha límite")
    print("8. Salir")   

def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor escribe un numero valido")
            
def guardar_tareas(tareas, archivo="tareas.json"):
    datos = []
    for tarea in tareas:
        if hasattr(tarea, "to_dict"):
            datos.append(tarea.to_dict())
        else:
            datos.append(tarea)
    
    with open("tareas.json", "w") as archivo:
        json.dump(datos, archivo, indent=1)  
    subir_backup("tareas.json")
        
def cargar_tareas():
    tareas = []
    if not os.path.exists("tareas.json"):
        return tareas

    with  open("tareas.json", "r") as archivo:
        datos = json.load(archivo)
        
        for item in datos:
            tipo = item.get("tipo", "Tarea")
            nombre = item.get("nombre")
            completada = item.get("completada", False)
            
            if tipo == "TareaConFecha":
                fecha_limite = item.get("fecha_limite", "")
                tarea = TareaConFecha(nombre, fecha_limite)
            else:
                tarea = Tarea(nombre)
    
            tarea.completada = completada
            tareas.append(tarea)
    return tareas
    