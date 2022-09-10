#Viernes 09/09/22
separador = "-----------------------\n"

print("Ejercicio 1")
print(separador)
#Crea un bucle for que imprima los valores del 7 al 14. Con una frase como esta: El valor del bucle es 7

for i in range(7,15):
    print(f"El valor del bucle es: {i}")

print(separador)


print("Ejercicio 2")
print(separador)
#Crea un bucle for que imprima los valores del 5 al 10. Con una frase como esta: El valor del bucle es 7

for i in range(5,11):
    print(f"El valor del bucle es: {i}")

print(separador)


print("Ejercicio 3")
print(separador)
#Crea un bucle for y luego un while que muestren una frase como las anteriores con los valores del 0 al -5000 en decrementos de 500.
print("Bucle For")
for i in range(0,-5000,-500):
    print(f"El valor del bucle es {i}")
print("Bucle While")
i=0
while i>(-5000):
    print(f"El valor del bucle es {i}")
    i=i-500

print("Ejercicio 4")
print(separador)
#Itera con un bucle, esta lista de países completamente.
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
for pais in paises:
    print(f"- {pais}")

print(separador)

print("Ejercicio 5")
print(separador)
#De la siguiente lista, con un bucle, itera todos sus valores y muestra una frase como «El valor del elemento es: 356».
#lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
# Quiero que omitas todos los valores 10.
# Además, quiero que rompas la ejecución del bucle cuando se encuentre el valor 356, pero se tienen que imprimir el resto de valores de la lista.

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
for numero in lista_numeros:
    if numero == 10:
        continue
    lista_numeros.sort()
    if numero == 356:
        break
    print(f"El {numero}")

print(separador)




