# importar clases
from estudiante import Estudiante
from calificacion import Calificacion

estudiantes = []

def registrar_estudiante():
    # nombre
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.strip() != "":
            break
        print("Nombre no válido. Intentelo de nuevo.\n")
    
    # matricula
    while True:
        matricula = input("Ingrese la matrícula: ")
        if matricula.strip() != "":
            break
        print("Matrícula no válida. Intentelo de nuevo.\n")
        
    # carrera
    while True:
        carrera = input("Ingrese la carrera: ")
        if carrera.strip() != "":
            break
        print("Carrera no válido. Intentelo de nuevo.\n")
        
    estudiante = Estudiante(nombre, matricula, carrera)
    
    for est in estudiantes:
        if est.matricula == estudiante.matricula:
            print("No es posible registrar la misma matricula")
            return
    
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito.\n")
    
def buscar_estudiante(matricula):
    for est in estudiantes:
        if est.matricula == matricula:
            return est
    return None

def asignar_calificacion():
    if estudiantes:
        # matricula
        while True:
            matricula = input("Ingrese la matrícula: ")
            if matricula.strip() != "":
                break
            print("Matrícula no válida. Intentelo de nuevo.\n")
            
        estudiante = buscar_estudiante(matricula)
        
        if estudiante:
            while True:
                materia = input("Ingrese la materia: ")
                if materia.strip() != "":
                    break
                print("Materia no valida.\n")
                
            while True:
                try:
                    nota = int(input(f"Ingrese la nota correspondiente a la materia {materia}: "))
                    if nota >= 0 and nota <= 10:
                        break
                    print("Nota no válida.\n")
                except ValueError:
                    print("Nota no válida.\n")
            
            # crea el objeto calificacion
            calificacion = Calificacion(materia, nota)
            
            estudiante.calificaciones.append(calificacion)
            
            print("¡Nota agregada con éxito!\n")
            
            
        else:
            print("Estudiante no encontrado.\n")
    else:
        print("No hay estudiantes registrados.\n")
        
def mostrar_estudiante():
    if estudiantes:
        # matricula
        while True:
            matricula = input("Ingrese la matrícula: ")
            if matricula.strip() != "":
                break
            print("Matrícula no válida. Intentelo de nuevo.\n")
            
        estudiante = buscar_estudiante(matricula)
        
        if estudiante:
            estudiante.mostrar_datos()
        else:
            print("Estudiante no encontrado.\n")
    else:
        print("No hay estudiantes registrados.\n")
        
def mostrar_todos():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
    for est in estudiantes:
        est.mostrar_datos()
        print("")