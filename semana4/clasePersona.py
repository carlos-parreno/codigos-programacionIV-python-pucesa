class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
        

persona1 = Persona("Carlos", 21)
persona2 = Persona("Ana", 30)

print(persona1.saludar())
print(persona2.saludar())


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        
    def datos_completos(self):
        return f"{self.saludar()}. Estudio {self.carrera}."
    
estudiante1 = Estudiante("Emily", 20, "Psicologia")

print(estudiante1.datos_completos())