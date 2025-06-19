class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False
        
    def mostrar(self, i):
        estado = "✅" if self.completada else "❌"
        print(f"{i+1}. {self.nombre} - {estado}")
        
    def to_dict(self):
        return{
            "tipo": "Tarea",
            "nombre": self.nombre,
            "completada": self.completada
        }