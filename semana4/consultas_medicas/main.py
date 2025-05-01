from funciones import registrar_pacientes, agregar_consulta, mostrar_paciente, mostrar_todos

def menu():
    while True:
        print("----- SISTEMA DE REGISTRO DE PACIENTES -----")
        print("1. Registrar nuevo paciente")
        print("2. Registrar consulta médica a un paciente")
        print("3. Mostrar datos de un paciente")
        print("4. Mostrar todos los pacientes")
        print("5. Salir")
        
        try:
            opcion = int(input("Ingrese una opción: "))
                   
        except ValueError:
            print("No es posible ingresar letras")
            print("Inténtelo nuevamente\n")
            continue
            
        if opcion == 1:
            registrar_pacientes()
        elif opcion == 2:
            agregar_consulta()
        elif opcion == 3:
            mostrar_paciente()
        elif opcion == 4:
            mostrar_todos()
        elif opcion == 5:
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
    
# ejecutar menu
if __name__ ==  "__main__":
    menu()