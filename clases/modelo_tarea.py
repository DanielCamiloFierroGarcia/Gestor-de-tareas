class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False
        
    def mostrar(self):
        estado = "✅" if self.completada else "❌"
        print(f"{self.nombre} - {estado}")