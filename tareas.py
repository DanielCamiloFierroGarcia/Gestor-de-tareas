from utilidades import pedir_entero, guardar_tareas

def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas")
    else:
        for i, t in enumerate(tareas):
            if t["completada"]:
                estado = "✅"
            else:
                estado = "❌"
            print(f"{i+1}. {t['nombre']} - {estado}")
            
def agregar_tareas(tareas):
    nombre = input("Escribe el nombre de la nueva tarea: ")
    tarea = {
        "nombre":nombre,
        "completada":False
    }
    tareas.append(tarea)
    print("Tarea agregada")
    guardar_tareas(tareas)
    
def completar_tarea(tareas):
    ver_tareas(tareas)
    i = pedir_entero("¿Qué número de tarea quieres marcar como completada? ") - 1
    if 0 <= i <len(tareas):
        tareas[i]["completada"] = True
        print("Tarea marcada como completada")
        guardar_tareas(tareas)
    else:
        print("Numero invalido")
        
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    i = pedir_entero("Que numero de tarea desea eliminar?: ") -1
    if 0<=i<len(tareas):
        while True:
            confirmacion = input(f"¿Seguro que quieres eliminar '{tareas[i]['nombre']}'? (s/n): ")
            if confirmacion.lower() == "s":
                eliminada = tareas.pop(i)
                print(f"Tarea '{eliminada['nombre']}' eliminada.")
                guardar_tareas(tareas)
                break
            elif confirmacion.lower() == "n":
                print("Eliminacion completa")
                break
            else:
                print("Ingresa una respuesta correscta: 's' o 'n'")
    else:
        print("Numero invalido")
        
def editar_tarea(tareas):
    ver_tareas(tareas)
    i = pedir_entero("Que numero de tarea quieres editar? ")-1
    if 0<=i<len(tareas):
        nuevo_nombre = input("Escribe el nuevo nombre de la tarea: ")
        tareas[i]["nombre"] = nuevo_nombre
        print("Tarea actualizada")
        guardar_tareas(tareas)
    else:
        print("Numero invalido")