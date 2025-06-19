from .modelo_tarea import Tarea
from datetime import datetime
        
class TareaConFecha(Tarea):
    def __init__(self, nombre, fecha_limite):
        super().__init__(nombre)
        self.fecha_limite = fecha_limite
        
    def mostrar(self, i):
        estado = "✅" if self.completada else "❌"
        print(f"{i+1}. {self.nombre} - {estado} (Límite: {self.fecha_limite})")
        
    def editar_fecha(self, nueva_fecha):
        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
            self.fecha_limite = nueva_fecha
            print("📅 Fecha límite actualizada.")
        except ValueError:
            print("❌ Formato inválido. Usa YYYY-MM-DD.")
        
    def to_dict(self):
        return{
            "tipo": "TareaConFecha",
            "nombre": self.nombre,
            "completada": self.completada,
            "fecha_limite": self.fecha_limite
        }