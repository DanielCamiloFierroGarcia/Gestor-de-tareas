import json
import os

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
        
def cargar_tareas():
    if os.path.exists("tareas.json"):
        try:
            with open("tareas.json", "r") as archivo:
                return json.load(archivo)
        except json.decoder.JSONDecodeError:
            print("El archivo 'tareas.json' esta dañado o mal formateado")
    else:
        return []