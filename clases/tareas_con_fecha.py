from .modelo_tarea import Tarea
        
class TareaConFecha(Tarea):
    def __init__(self, nombre, fecha_limite):
        super().__init__(nombre)
        self.fecha_limite = fecha_limite
        
    def mostrar(self, i):
        estado = "✅" if self.completada else "❌"
        print(f"{i+1}. {self.nombre} - {estado} (Límite: {self.fecha_limite})")
        
    def to_dict(self):
        return{
            "tipo": "TareaConFecha",
            "nombre": self.nombre,
            "completada": self.completada,
            "fecha_limite": self.fecha_limite
        }