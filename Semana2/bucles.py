"""
# for en ciclos
print("Ingreso por teclado")

numero = int(input("Ingrese un numero: "))

for i in range(numero + 1):
    print(i)
    
for i in [1,2,3]: #lista
    print(i) # O(n) lineal
"""
""" 
for i in range(0, 6):
    print("tabla del", i)
    for j in range(0, 11):
        print(f"{i} x {j} = {i*j}")
"""
        
     
# a = 5   # inicializar 
# while a > 0:
#     print(a)
#     a -= 1    
    

# print("Lista de -10 a 10 con while identicando que numero es para o impar")

# a = -10

# while a < 11:
#     if a % 2 == 0:
#         print(f"{a} es par")
#     else:
#         print(f"{a} es impar")
#     a += 1
    
# def nombre():
#     nombre = input("Introduce tu nombre")
#     return nombre

# print(nombre()) # invocar a la funcion, parametro tiene el valor del agumento, argumento es la variable

#Argumento posicionales = ss asocian a los parametros en el mismo orden que aparecen en el mismo orden de la definicion de la funcion 
# Argumentos nominales = se indica explicitamente el nombre del parametro al que se asocia un agumento de la forma parametro = argumento
# parametro argumento = clave - valor

# def usuario(nombre, edad):
#     print(f"Hola {nombre} tienes {edad} años")
    
# usuario("Carlos", 21) #posicional
# usuario(nombre = "Juan", edad = "17")
# usuario(edad = 40, nombre = "Dalia")

# # argumentos por defecto
# #def welcome(nombre, edad, nacionalidad = "Ecuatoriano")

# print("***Pasar un numero indeterminado de argumentos***")

#def contacto(**info)

print("Programa para multiplicar n numeros consecutivos")
def multiplicar(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

resultado = multiplicar(10,20,30,40,50,60,70,80,90,100) # 10*20*30*40*50*60*70*80*90*100 = 3628800000000
print(resultado)