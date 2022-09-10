#Lunes 05/09/22
#Impirmir en consola «Estoy en el día 1 del reto de Python.»
print("«Estoy en el día 1 del reto de Python.»")
print("--------------------------")

##################
texto = "«Estoy en el día 1 del reto de Python.»"

print(texto)
print("--------------------------")

#################
a = "rojo"
b = "naranja"
c = "azul"
d = "verde"

a = d

print(a)
print("------------------------")

frase_1 = "Me llamo Sandra"
frase_2 = "y tengo 23 años."

print(f"{frase_1} {frase_2}")

#Proyecto día 1
#  Debes construir un programa que haga lo siguiente:
#
# Frase de saludo inicial.
# Entrada del usuario preguntando el nombre.
# Entrada del usuario preguntando la edad.
# Entrada del usuario preguntando el país de nacimiento.
# Comentarios en cada sección del código (tú pon donde creas necesario, no temas equivocarte aquí).
# Vas a tener que presentar los datos recogidos del usuario e imprimirlos en una frase final.
# Debes utilizar saltos de línea en todo el código, donde consideres necesario para que todo quede lo mejor presentado posible en la consola.

#Saludo de bienvenida
saludo = "Hola, este es un programada de Bienvenida."
#Inputs de texto para preguntar al usuario y guardar datos en variables
nombre = input("Por favor, dime tu nombre: ")
edad = input("Por favor, dime tu edad: ")
pais = input("Por favor, dime tu pais de nacimiento: ")

print(f"""
    Hola {nombre}, usted tiene {edad} años y nació en {pais}
""")


