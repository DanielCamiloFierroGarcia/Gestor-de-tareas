# Gestor-de-tareas
Gestor de tareas en python: objetivo crear un organizador de tareas que permita añadir/modificar/eliminar/marcar como completado. 

Hasta el momento:
- Agregar (y con fecha límite)/modificar/eliminar tareas
- Marcar tarea como completada
- Almacenar tareas registradas en archivo JSON
- Filtrar tareas por estado
- Crear backup del archivo en AWS: S3 y descargar dicho el descargar backup
- Creacion de clases para agregar POO al proyecto
- Creacion de tareas con fecha y agregar al JSON (pasar de utilizar diccionarios como modelo de datos a objetos tipo clases)

## Cómo usar

```bash
python "gestor tareas".py

## Requisitos

- Python 3.10+
- boto3 (para respaldo en AWS)
