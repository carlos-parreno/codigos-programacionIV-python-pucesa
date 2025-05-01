import datetime
# importar la clase Paciente del archivo paciente.py
from paciente import Paciente


# lista global para pacientes
pacientes = []

# CONSTANTES
LISTA_TIPOS_SANGRE = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# funciones

def registrar_pacientes():
    # nombre
    while True:
        nombre = input("Ingrese el nombre del paciente que desea registrar: ")
        if nombre.strip() != "":
            break
        print("No puede ingresar espacios en blanco como nombre")
        print("Inténtelo nuevamente")
    
    # cedula
    while True:
        cedula = input("Ingrese la cédula del paciente que desea registrar: ")
        if len(cedula) == 10 and cedula.isdigit():
            break
        print("La cédula tiene 10 digitos numericos")
        print("Inténtelo nuevamente")
            
    # edad
    while True:
        try:
            edad = int(input("Ingrese la edad del paciente que desea registrar: "))
            if edad > 0 and edad <= 100:
                break
            print("La edad tiene que estar entre 1 y 100 años")
            print("Inténtelo nuevamente")
        except ValueError:
            print("La edad tiene que ser un numero")
            print("Inténtelo nuevamente ")
       
    
    # tipoSangre
    while True:
        print("Los tipos de sangre son: A+, A-, B+, B-, AB+, AB-, O+, O-")
        tipoSangre = input("Ingrese el tipo de sangre del paciente que desea registrar: ")
        if tipoSangre in LISTA_TIPOS_SANGRE:
            break
        print("Debe ingresar una opción de la lista. Inténtelo nuevamente")
    
    # crear un paciente
    paciente = Paciente(nombre, cedula, edad, tipoSangre)
    
    bandera = True
    for pac in pacientes:
        if pac.cedula == paciente.cedula:
            print("No es posible registrar cedulas repetidas.\n")
            bandera = False
            
    if bandera == True:
        # almacenar paciente
        pacientes.append(paciente) 
        print("Paciente registrado con éxito.\n")
    
def buscar_paciente(cedula):
    for pac in pacientes:
        if pac.cedula == cedula:
            return pac
    return None

def agregar_consulta():
    # cedula
    while True:
        cedula = input("Ingrese la cédula del paciente que desea buscar: ")
        if len(cedula) == 10 and cedula.isdigit():
            break
        print("La cédula tiene 10 digitos numericos")
        print("Inténtelo nuevamente")
        
    paciente = buscar_paciente(cedula)
        
    if paciente:
        # fecha
        while True:
            try:
                fecha = input("Ingrese una fecha: ")
                datetime.datetime.strptime(fecha, "%d/%m/%Y")
                break
            except ValueError:
                print("El formato de la fecha es DD/MM/YYYY")
                print("Inténtelo nuevamente")
        
        # diagnostico
        while True:
            diagnostico = input("Ingrese el diagnostico: ")
            if diagnostico.strip != "":
                break
            print("No puede ingresar unicamente espacios en blanco")
            print("Inténtelo nuevamente")
        # tratamiento
        while True:
            tratamiento = input("Ingrese el tratamiento: ")
            if tratamiento.strip != "":
                break
            print("No puede ingresar unicamente espacios en blanco")
            print("Inténtelo nuevamente")
            
        diccionario = {
            "Fecha": fecha,
            "Diagnostico": diagnostico,
            "Tratamiento": tratamiento        
        }
        
        paciente.agregar_consulta(diccionario)
        print("Consulta agregada exitosamente\n")
        
    else:
        print("Paciente no encontrado\n")
        
        
def mostrar_paciente():
    # cedula
    while True:
        cedula = input("Ingrese la cédula del paciente que desea buscar: ")
        if len(cedula) == 10 and cedula.isdigit():
            break
        print("La cédula tiene 10 digitos numericos")
        print("Inténtelo nuevamente")
        
    paciente = buscar_paciente(cedula)
    
    if paciente:
        paciente.mostrar_datos()
    else:
        print("Paciente no encontrado\n")
        
def mostrar_todos():
    if not pacientes:
        print("No hay pacientes registrados \n")
    for pac in pacientes:
        pac.mostrar_datos()
        print("")