print("\n\t\t\tCalculadora\n")

print("""\n\t\t\tMenú
      1. Suma
      2. Resta
      3. Multiplicación
      4. División\n""")

opcion = int(input("Elige una opcion: "))

if opcion >= 1 and opcion <= 4:
    
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    if opcion == 1: 
        print("Usted ha seleccionado suma")
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
        
    elif opcion == 2:
        print("Usted ha seleccionado resta")
        print(f"{numero1} - {numero2} = {numero1 - numero2}")
    elif opcion == 3:
        print("Usted ha seleccionado multiplicación")
        print(f"{numero1} * {numero2} = {numero1*numero2}")
    else:
        print("Usted ha seleccionado división")  
        if numero2 != 0:
            print(f"{numero1}/{numero2} = {numero1/numero2}")
        else:
            print("No se puede dividir por 0")
else:
    print("Solo puede seleccionar una opción entre 1 y 4")
    
    
print("\nPrograma realizado por Carlos Parreño")



numero = int(input("Ingrese un número: "))

