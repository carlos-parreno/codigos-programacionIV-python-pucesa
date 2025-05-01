# clase reserva
class Reserva:
    # constructor
    def __init__(self, fecha_entrada, fecha_salida, tipo_habitacion):
        # atributos
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.tipo_habitacion = tipo_habitacion
        
    def mostrar_datos(self):
        print(f"Fecha entrada: {self.fecha_entrada}")
        print(f"Fecha salida: {self.fecha_salida}")
        print(f"Tipo habitación: {self.tipo_habitacion}")