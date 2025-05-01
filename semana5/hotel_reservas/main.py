# importar clases
from funciones import registrar_huesped, agregar_reserva, mostrar_todas_reservas, mostrar_todos_huespedes

while True:
    print("----- RESERVAS EN UN HOTEL -----")
    print("1. Registrar nuevo huesped")
    print("2. Registrar reserva a un huesped")
    print("3. Mostrar todas las reservas")
    print("4. Mostrar todos los huespedes")
    print("5. Salir\n")
    
    opcion = input("Ingrese una opción: ")
    print("")
    
    # registrar nuevo huesped
    if opcion == "1":
        registrar_huesped()
    # crear reserva para un huesped existente
    elif opcion == "2":
        agregar_reserva()
    # mostrar todas las reservas registradas
    elif opcion == "3":
        mostrar_todas_reservas()
    # mostrar todos los huespedes registrados
    elif opcion == "4":
        mostrar_todos_huespedes()
    # salir
    elif opcion == "5":
        print("Gracias por usas el sistema. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida.\n")
        