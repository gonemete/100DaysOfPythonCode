#Jueves 08/09/22
separador = "-----------------------\n"

print("Ejercicio 1")
print("-----------------------")
#Crea una lista llamada «lista_numeros» y almacena los siguientes valores integer: 10,45,55,76
lista_numeros = [10,45,55,76]
print(lista_numeros)
print(separador)


print("Ejercicio 2")
print("-----------------------")
#De la lista anterior, imprime el valor 76 en la consola.
print(lista_numeros[-1])
print(separador)

print("Ejercicio 3")
print("-----------------------")
#Utiliza el formateo de strings (f»») para imprimir esta frase en la consola. Utiliza la lista del ejercicio 1 para mostrar el 10 y el 76.
print(f"El valor más pequeño en la lista es {lista_numeros[0]} y el más grande es {lista_numeros[-1]}")
print(separador)


print("Ejercicio 7")
print("-----------------------")
#Imprime en la consola el carácter «u» de azul.
lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[1][2])
print(separador)


print("Ejercicio 8")
print(separador)
#Este es un listado de países. Imprime los dos últimos países, Zambia y Zimbabwe.
paises = ["Afghanistan","Albania","Algeria",
"Andorra","Angola","Anguilla",
"Antigua and Barbuda",
"Argentina","Armenia",
"Aruba","Australia","Austria",
"Azerbaijan","Bahamas","Bahrain",
"Bangladesh","Barbados","Belarus",
"Belgium","Belize","Benin","Bermuda",
"Bhutan","Bolivia","Bosnia & Herzegovina",
"Botswana","Brazil","British Virgin Islands",
"Brunei","Bulgaria","Burkina Faso","Burundi",
"Cambodia","Cameroon","Cape Verde",
"Cayman Islands","Chad","Chile","China",
"Colombia","Congo","Cook Islands",
"Costa Rica","Cote D Ivoire","Croatia",
"Cruise Ship","Cuba","Cyprus","Czech Republic",
"Denmark","Djibouti","Dominica",
"Dominican Republic","Ecuador","Egypt",
"El Salvador","Equatorial Guinea",
"Estonia","Ethiopia","Falkland Islands",
"Faroe Islands","Fiji","Finland","France",
"French Polynesia","French West Indies","Gabon",
"Gambia","Georgia","Germany","Ghana","Gibraltar",
"Greece","Greenland","Grenada","Guam","Guatemala",
"Guernsey","Guinea","Guinea Bissau","Guyana",
"Haiti","Honduras","Hong Kong","Hungary","Iceland",
"India","Indonesia","Iran","Iraq","Ireland",
"Isle of Man","Israel","Italy","Jamaica","Japan",
"Jersey","Jordan","Kazakhstan","Kenya","Kuwait",
"Kyrgyz Republic","Laos","Latvia","Lebanon",
"Lesotho","Liberia","Libya","Liechtenstein",
"Lithuania","Luxembourg","Macau","Macedonia",
"Madagascar","Malawi","Malaysia","Maldives",
"Mali","Malta","Mauritania","Mauritius","Mexico",
"Moldova","Monaco","Mongolia","Montenegro",
"Montserrat","Morocco","Mozambique","Namibia",
"Nepal","Netherlands","Netherlands Antilles",
"New Caledonia","New Zealand","Nicaragua","Niger",
"Nigeria","Norway","Oman","Pakistan","Palestine",
"Panama","Papua New Guinea","Paraguay","Peru",
"Philippines","Poland","Portugal","Puerto Rico",
"Qatar","Reunion","Romania","Russia","Rwanda",
"Saint Pierre & Miquelon","Samoa","San Marino",
"Satellite","Saudi Arabia","Senegal","Serbia",
"Seychelles","Sierra Leone","Singapore","Slovakia",
"Slovenia","South Africa","South Korea","Spain",
"Sri Lanka","St Kitts & Nevis","St Lucia",
"St Vincent","St. Lucia","Sudan","Suriname","Swaziland",
"Sweden","Switzerland","Syria","Taiwan","Tajikistan",
"Tanzania","Thailand","Timor L'Este","Togo","Tonga",
"Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine",
"United Arab Emirates","United Kingdom","Uruguay",
"Uzbekistan","Venezuela","Vietnam",
"Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
print(paises[-1], paises[-2])
print(separador)

print("Ejercicio 9")
print(separador)
#Añade a la lista_colores los siguientes colores en los sitios donde se te pide. Lo tienes que hacer con algún método de adición de elementos, no puedes editar la lista manualmente. Tienes que añadir los colores en el código en este orden:
# - gris – Antes de «rojo».
# - rosa – En último lugar.
# - naranja – Entre «azul» y «verde».
lista_colores = ["rojo", "azul", "verde", "amarillo"]

lista_colores.insert(0,"gris")
lista_colores.insert(3,"naranja")
lista_colores.append("rosa")
print(lista_colores)
print(separador)

print("Ejercicio 10")
print(separador)
#De la lista resultante del ejercicio anterior, elimina los valores «rojo», «verde» y «amarillo» con el método pop().
lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)
print(lista_colores)
print(separador)

print("Ejercicio 11")
print(separador)
lista_colores = ["rojo", "azul", "verde", "amarillo"]
nueva_lista_colores = lista_colores
print(nueva_lista_colores)
print(separador)

print("Ejercicio 12")
print(separador)
#¿Sabrías hacer que Python te diga cuántas repeticiones del valor 10 hay en esta lista?
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
print(lista_numeros.count(10))
print(separador)

print("Ejercicio 13")
print(separador)
#Emplea un método de Python que muestre la posición del valor «Brazil» de la lista de países del ejercicio 8.
print(paises.index("Brazil"))
print(separador)


print("Ejercicio 14")
print(separador)
#Ordena la lista_numeros del ejercicio 12 de menor a mayor.
lista_numeros.sort()
print(lista_numeros)
print(separador)

print("Ejercicio 15")
print(separador)
lista_numeros.sort(reverse=True)
print(lista_numeros)
#Ordena la lista_numeros del ejercicio 12 de mayor a menor.
print(separador)

print("Ejercicio 16")
print(separador)
#Muéstrame en la consola, la longitud en número de posiciones de la lista de países del ejercicio 8 con un método.
print(len(paises))
