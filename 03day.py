#Miércoles 07/09/22

#Poner operadores logicos para que la expresión sea True

print("Ejercicio 1 al 5")
print("-----------------------")

numero = 10
if numero > 7:
    print("Verdadero")

print("-----------------------")

numero= 5
if numero<7:
    print("Verdadero")

print("-----------------------")

numero = 7
if numero == 7:
    print("Verdadero")

print("-----------------------")

color = "verde"
forma = "triangular"

if color == "verde" and forma == "triangular":
    print("Verdadero.")
else:
    print("Falso.")

print("-----------------------")

color = "rojo"
forma = "círculo"
tamano = "pequeño"

if color == "rojo" and forma == "círculo" or tamano == "grande":
    print("Verdadero.")
else:
    print("Falso.")

print("-----------------------")
#print("Ejercicio 6")
# ¿Es cierta esta afirmación? El bloque else, nunca lleva expresión de comparación. Está sujeto a las expresiones del if y elif si los hay.
#RESPUESTA: SI

print("------------ PROYECTO CALCULADORA ------------\n")
print("""
################### CALCULADORA AVANZADA ###################
############################################################
""")


operacion = input("""
Por favor, indique la operación que desea realizar:
1 - SUMA
2 - RESTA
3 - MULTIPLICACION
4 - DIVISION
5 - MÓDULO
6 - EXPONENTE\n
""")
operacion=int(operacion)
if operacion >=1 and operacion <=6:
    if operacion == 1:
        print("Ha elegido Sumar")
    if operacion == 2:
        print("Ha elegido Restar")
    if operacion == 3:
        print("Ha elegido Multiplicar")
    if operacion == 4:
        print("Ha elegido Dividir")
    if operacion == 5:
        print("Ha elegido Módulo")
    if operacion == 6:
        print("Ha elegido Exponente")
else:
    print("No ha elegido correctamente, vuelva a elegir")

num1=float(input("Escriba el primer numero\n"))
num2=float(input("Escriba el segundo numero\n"))

if operacion == 1:
    resultado = num1+num2
    print(f"Resultado = {resultado}")
if operacion == 2:
    resultado = num1-num2
    print(f"Resultado = {resultado}")
if operacion == 3:
    resultado = num1*num2
    print(f"Resultado = {resultado}")
if operacion == 4:
    resultado = num1/num2
    print(f"Resultado = {resultado}")
if operacion == 5:
    resultado = num1%num2
    print(f"Resultado = {resultado}")
if operacion == 6:
    resultado = num1**num2
    print(f"Resultado = {resultado}")

print("-----------------------")
print("-----------------------")
print("-----------------------")
print("-----------------------")
