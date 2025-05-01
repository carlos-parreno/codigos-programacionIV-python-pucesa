# importar clases
from funciones import registrar_estudiante, asignar_calificacion, mostrar_estudiante, mostrar_todos
def menu():
    while True:
        print("----- SISTEMA DE REGISTRO ACADEMICO -----")
        print("1. Registrar nuevo estudiante")
        print("2. Asignar calificación a un estudiante")
        print("3. Mostrar información de un estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir\n")
        
        opcion = input("Ingrese una opción: ")
        print("")
        
        # registrar nuevo estudiante
        if opcion == "1":
            registrar_estudiante()
        # asignar calificación a un estudiante"
        elif opcion == "2":
            asignar_calificacion()
        # mostrar información de un estudiante
        elif opcion == "3":
            mostrar_estudiante()
        # mostrar todos los estudiantes
        elif opcion == "4":
            mostrar_todos()
        # salir
        elif opcion == "5":
            print("Gracias por usas el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.\n")
            

# ejecutar menu
if __name__ ==  "__main__":
    menu()
        