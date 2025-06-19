from .modelo_tarea import Tarea
        
class TareaConFecha(Tarea):
    def __init__(self, nombre, fecha_limite):
        super().__init__(nombre)
        self.fecha_limite = fecha_limite
        
    def mostrar(self):
        estado = "✅" if self.completada else "❌"
        print(f"{self.nombre} - {estado} - Fecha límite: {self.fecha_limite}")
        