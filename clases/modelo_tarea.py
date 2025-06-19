class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False
        
    def mostrar(self):
        estado = "✅" if self.completada else "❌"
        print(f"{self.nombre} - {estado}")
        
    def to_dict(self):
        return{
            "tipo": "Tarea",
            "nombre": self.nombre,
            "completada": self.completada
        }