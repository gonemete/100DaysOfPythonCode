#Domingo 11/09/2022

separador = "-----------------------\n"

print("Ejercicio 1")
print(separador)
#Añade cualquier color con un input al principio de la lista mediante una función. Debes comprobar fuera de la función, con un print(), que el color se ha añadido correctamente.
colores = ["rojo", "verde", "amarillo"]

def addColor(color):
    colores.insert(0,color)

addColor("azul")

print(colores)

print(separador)
print("Sólo es un ejercicio + Proyecto")

