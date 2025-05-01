# clase Huesped
class Huesped:
    # constructor
    def __init__(self, nombre, cedula, correo_electronico):
        # atributos
        self.nombre = nombre
        self.cedula = cedula
        self.correo_electronico = correo_electronico
        self.reservas = []
        
    # agregar una reserva al huesped
    def agregar_reservas(self, reserva):
        self.reservas.append(reserva)
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Correo electrónico: {self.correo_electronico}")