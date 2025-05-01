# importar librerias
import datetime
# importar clases
from huesped import Huesped
from reserva import Reserva
# lista global para huespedes
huespedes = []

def registrar_huesped():
    # nombre
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.strip() != "":
            break
        print("Nombre no válido. Intentelo de nuevo.\n")
    
    # cedula
    while True:
        cedula = input("Ingrese la cédula: ")
        if len(cedula) == 10 and cedula.isdigit():
            break
        print("Cédula inválida. Intentelo de nuevo.\n")
        
    # correo
    correo_electronico = input("Ingrese el correo electrónico: ")
    
    # creacion del objeto huesped
    huesped = Huesped(nombre, cedula, correo_electronico)
    
    
    for hues in huespedes:
        if hues.cedula == huesped.cedula:
            print("No se pueden registrar cédulas repetidas.\n")
            return
            
    # añadir el huesped a la lista global de huespedes
    huespedes.append(huesped)
    print("Huesped registrado con éxito.\n")
            
def buscar_huesped(cedula):
    for hues in huespedes:
        if hues.cedula == cedula:
            return hues
    return None
    
def agregar_reserva():
    # cedula
    while True:
        cedula = input("Ingrese la cédula: ")
        if len(cedula) == 10 and cedula.isdigit():
            break
        print("Cédula inválida. Intentelo de nuevo.\n")
        
    huesped = buscar_huesped(cedula)
    
    if huesped:
        # fecha entrada
        while True:
            try:
                fecha_entrada = input("Ingrese la fecha de entrada: ")
                datetime.datetime.strptime(fecha_entrada, "%d/%m/%Y")
                break
            except ValueError:
                print("El formato de la fecha es DD/MM/YYYY\n")
                
                
        # fecha salida
        while True:
            try:
                fecha_salida = input("Ingrese la fecha de salida: ")
                datetime.datetime.strptime(fecha_salida, "%d/%m/%Y")
                break
            except ValueError:
                print("El formato de la fecha es DD/MM/YYYY\n")
            
            
        # tipo habitacion
        tipo_habitacion = input("Ingrese el tipo de habitación: ")
        
        reserva = Reserva(fecha_entrada, fecha_salida, tipo_habitacion)
        
        huesped.reservas.append(reserva)
        
        print("¡Reserva registrada con éxito!\n")
    else:
        print("Huesped no encontrado.\n")
        
def mostrar_todas_reservas():
    if not huespedes:
        print("No hay huespedes registrados.\n")
        
    for hues in huespedes:
        print(f"Cliente: {hues.cedula}")
        for res in hues.reservas:
            res.mostrar_datos()
            print("")
        
        
def mostrar_todos_huespedes():
    if not huespedes:
        print("NO hay huespedes registrados.\n")
    for hues in huespedes:
        hues.mostrar_datos()
        print("")