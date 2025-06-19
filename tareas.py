from utils.utilidades import pedir_entero, guardar_tareas, descargar_backup
from clases.tareas_con_fecha import TareaConFecha
from clases.modelo_tarea import Tarea

def ver_tareas(tareas):
    for i, t in enumerate(tareas):
        t.mostrar(i)        
            
def agregar_tareas(tareas):
    nombre = input("Escribe el nombre de la nueva tarea: ")
    tarea = Tarea(nombre)
    tareas.append(tarea)
    print("Tarea agregada")
    guardar_tareas(tareas)
    
def completar_tarea(tareas):
    ver_tareas(tareas)
    i = pedir_entero("¿Qué número de tarea quieres marcar como completada? ") - 1
    if 0 <= i <len(tareas):
        tareas[i].completada = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada")
    else:
        print("Numero invalido")
        
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    i = pedir_entero("Que numero de tarea desea eliminar?: ") -1
    if 0<=i<len(tareas):
        while True:
            confirmacion = input(f"¿Seguro que quieres eliminar '{tareas[i].nombre}'? (s/n): ")
            if confirmacion.lower() == "s":
                eliminada = tareas.pop(i)
                print(f"Tarea '{eliminada.nombre}' eliminada.")
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
        tareas[i].nombre = nuevo_nombre
        print("Tarea actualizada")
        guardar_tareas(tareas)
    else:
        print("Numero invalido")
        
def descargar_backups_desde_s3():
    fecha = input("📅 Fecha del backup (YYYY-MM-DD): ").strip()
    confirmar = input("⚠️ Esto sobrescribirá tu archivo local. ¿Continuar? (s/n): ")
    if confirmar.lower() == "s":
        descargar_backup(fecha, "tareas.json")
        
def agregar_tarea_con_fecha(tareas):
    nombre = input("📝 Nombre de la tarea: ")
    fecha = input("📅 Fecha límite (YYYY-MM-DD): ")
    tarea = TareaConFecha(nombre, fecha)
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("✅ Tarea con fecha agregada.")
    
def mostrar_tareas_filtradas(tareas, estado=None):
    print(type(tareas[0]))
    """
    Muestra tareas dependiendo del estado.
    - estado = None => todas
    - estado = True => solo completadas
    - estado = False => solo pendientes
    """
    tareas_filtradas = (
        tareas if estado is None else [t for t in tareas if t.completada == estado]
    )
    
    if not tareas_filtradas:
        print("📭 No hay tareas para mostrar.")
        return
    for i, tarea in enumerate(tareas_filtradas, 1):
        estado_icono = "✅" if tarea.completada else "❌"
        print(f"{i}. {tarea.nombre} {estado_icono}")