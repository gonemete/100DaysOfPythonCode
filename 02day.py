#Martes 06/09/22
#Cuales de estos strings son correctos?
# "Hoy es un gran día para programar"
# 'El cielo está nublado"
# '¿Qué día es hoy?'
# "Mañana, en inglés se dice "morning""

#El primero y el tercero son correctos
# print("Mañana, en inglés se dice "morning"")
#Para el segundo y el cuarto el error es SyntaxError

#Imprime el numero de caracteres de la palabra "automaticamente"
print("Ejercicio 3")
texto = "Automáticamente"
print(len(texto))
print("""
--------------------
--------------------
""")
#Imprime sólo la a acentuada de automaticamente
print("Ejercicio 4")
print(texto[5])
print("""
--------------------
--------------------
""")
#Haz 10 elevado a 5 con exponente
print("Ejercicio 5")
print(10**5)
print("""
--------------------
--------------------
""")
#Haz 10 elevado a 5 sin exponente
print("Ejercicio 6")
print(10*10*10*10*10)
print("""
--------------------
--------------------
""")
#En que dos estados puede estar un booleano
booleano=True
booleano=False

#Muestra en consola el tipo de dato de la variable numero_1
print("Ejercicio 8")
numero_1=675.87
print(type(numero_1))
print("""
--------------------
--------------------
""")
#Muestra el numero de digitos del número 768763843 con len()
print("Ejercicio 9")
print(len("768763843"))
print("""
--------------------
--------------------
""")
#Haz que estos datos float se conviertan en integer
print("Ejercicio 10")
numero_1 = "14.527"
numero_2 = "560.92"
#Esto lo tuve que mirar:
#No se puede hacer directamente. Hay que pasar primero a Float y luego a Int
numero_1=float("14.527")
numero_2=float("560.92")
print(int(numero_1))
print(int(numero_2))
print("""
--------------------
--------------------
""")


#Redondea estos numero
print("Ejercicio 11")
numero_1 = 10.897654876534 # 3 decimales
numero_2 = 7674.7886 # 2 decimales 
numero_3 = 68754.78 # 1 decimal

print(round(numero_1,3))
print(round(numero_2,2))
print(round(numero_3,1))
print("""
--------------------
--------------------
""")
#Diferencia entre módulo y floor division
#El módulo % es el resto de la división 8%2 el módulo = 0
#Floor division es el cociente de la división 21//5 el resultado es 4


#Asigna con los operadores de asignación de incremento o decremento los siguientes valores indicados en los comentarios.
print("Ejercicio 12")
numero_1 = 10 # +60
numero_2 = 24 # -100
numero_3 = 65.67 # +4.33

#Esto es como yo lo he hecho a lo bruto
print(10+60)
print(24-100)
print(65.67+4.33)

#Se hace así
numero_1+=60
numero_2-=100
numero_3+=4.33

print(numero_1)
print(numero_2)
print(numero_3)
print("""
--------------------
--------------------
""")
#Concatena con f strings
print("Ejercicio 13")
print(f"{numero_1}, {numero_2}, {numero_3}")
valor=769.97
valor2=4
texto="Am I a string?"
respuesta=True
print(f"El valor {valor} es bastante más grande que {valor2}. {texto} The Answer is {respuesta}")
print("""
--------------------
--------------------
""")
#Proyecto
#Calculadora de exponentes
print("---- Calculadora de exponentes ----")
numero=int(input("Introduzca el primer numero\n"))
exponente=int(input("Introduzca el segundo número\n"))
resultado=numero**exponente
print(f"El resultado de {numero} elevado a {exponente} es igual a {resultado}")
