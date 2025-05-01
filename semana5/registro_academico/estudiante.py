# clase estudiante
class Estudiante:
    # constructor
    def __init__(self, nombre, matricula, carrera):
        # atributos
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []
        
    def agregar_calificacion(self, materia_nota):
        self.calificaciones.append(materia_nota)
        
    def mostrar_calificaciones(self):
        for calif in self.calificaciones:
            calif.mostrar_datos()
        print("")
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Matricula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print("Calificaciones")
        self.mostrar_calificaciones()