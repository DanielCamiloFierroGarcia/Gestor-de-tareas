import json
import os
from s3_utils import subir_backup, descargar_backup

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Ver tareas")
    print("2. Agregar tarea") 
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Editar tarea")
    print("6. Restaurar tareas desde backup")
    print("7. Salir")   

def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor escribe un numero valido")
            
def guardar_tareas(tareas):
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)  
    subir_backup("tareas.json")
        
def cargar_tareas():
    if os.path.exists("tareas.json"):
        try:
            with open("tareas.json", "r") as archivo:
                return json.load(archivo)
        except json.decoder.JSONDecodeError:
            print("El archivo 'tareas.json' esta dañado o mal formateado")
    else:
        return []