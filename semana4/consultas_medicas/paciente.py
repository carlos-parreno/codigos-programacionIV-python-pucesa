# clase Paciente
class Paciente:
    # constructor
    def __init__(self, nombre, cedula, edad, tipoSangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipoSangre = tipoSangre
        self.consultas = []
        
    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)
                
    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.tipoSangre}")
        print("Consultas\n")
        for i in range(len(self.consultas)):
            print(f"{self.consultas[i]}")