###############################################################
########################## PROYECTO ###########################
# El proyecto va a ser un pequeño programa de consola que permita al usuario hacer un pedido de pizza con ingredientes extra para añadir.

# Requisitos del proyecto
# Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
print("""
##############################################################################
############################    PIZZERIA PY    ###############################
############################                   ###############################
##############################################################################\n
""")


# El usuario introducirá el dinero que quiera. Guárdalo en una variable.
dinero_usuario=float(input("Por favor indica el importe del que dispones: "))
gasto=0
gasto_total=0
saldo=dinero_usuario-gasto_total

# Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
ingredientes=[]
gastos=[]
nota_final=[]
nombre_extra_1="Atún"
precio_extra_1=2
nombre_extra_2="Anchoas"
precio_extra_2=3
nombre_extra_3="Peperoni"
precio_extra_3=2.75


# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
PIZZA_MARGARITA = 10.00
PIZZA_ATUN = 14.00
PIZZA_4QUESOS = 16.50

# El usuario podrá elegir solo una pizza.
print("Por favor, elige sólo 1 pizza:\n" )
print(f"""
Disponemos de las siguientes pizzas:
1-Margarita ................ {PIZZA_MARGARITA}€
2-Atún ..................... {PIZZA_ATUN}€
3-Cuatro Quesos ............ {PIZZA_4QUESOS}\n
""")

eleccion=int(input("Por favor, indica el número de la Pizza deseada: \n"))

if eleccion==1:
    print(f"Usted ha elegido una Pizza Margarita")
    gastos.append(PIZZA_MARGARITA)
    ingredientes.append("Pizza Margarita")
if eleccion==2:
    print(f"Usted ha elegido una Pizza de Atún")
    gastos.append(PIZZA_ATUN)
    ingredientes.append("Pizza de Atún")
if eleccion==3:
    print(f"Usted ha elegido una Pizza 4 Quesos")
    gastos.append(PIZZA_4QUESOS)
    ingredientes.append("Pizza 4 Quesos")
    


# Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
print(f"*- Tu gasto total es de {gastos[0]} euros. Actualmente dispones de {dinero_usuario-gastos[0]} euros de saldo.\n")

#En caso de que nos pasemos vamos a crear un bucle para pedir bien
#ESTO NO ESTÁ HECHO TODAVÍA

# Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
print("*- Usted puede solicitar más ingredientes extra. Esto aumentará el precio final\n")
print(f"""Los ingredientes a elegir son:
{nombre_extra_1}: {precio_extra_1}€
{nombre_extra_2}: {precio_extra_2}€
{nombre_extra_3}: {precio_extra_3}€\n
""")
anadir_extra=input("** - Desea añadir algún extra?: \n")

if anadir_extra.lower() == "si":
    valor_extra=True
if anadir_extra.lower() == "no":
    valor_extra=False

#print(f"Imprimimos el gasto total has ahora {gasto_total}")

while valor_extra:
    componente=input("*- Por favor añade el componente que deseas: ")
    
    if componente=="Atún":
        print(f"Gasto del atún {precio_extra_1}")
        gastos.append(precio_extra_1)
        ingredientes.append(componente)
        print(f"*- Te has gastado {sum(gastos)} euros. Te quedan {(dinero_usuario)-sum(gastos)}€")
    if componente=="Anchoas":
        print(f"Gasto de las Anchoas {precio_extra_2}")
        gastos.append(precio_extra_2)
        ingredientes.append(componente)
        print(f"*- Te has gastado {sum(gastos)} euros. Te quedan {(dinero_usuario)-sum(gastos)}€")
    if componente=="Peperoni":
        print(f"Gasto del Peperoni {precio_extra_3}")
        gastos.append(precio_extra_3)
        ingredientes.append(componente)
        print(f"*- Te has gastado {sum(gastos)} euros. Te quedan {(dinero_usuario)-sum(gastos)}€")
    componente = input("** - Desea añadir alguno más?")
    # print(f"Has ahora el gasto total es de {sum(gastos)}")
    # print(f"Te has gastado {sum(gastos)} euros. Te quedan {(dinero_usuario)-sum(gastos)}€")
    if componente=="no":
        valor_extra=False

if dinero_usuario<sum(gastos):
    print("*** Atención has sobrepasado tu presupuesto. Vuelve a hacer el pedido ***\n")
else:
    if len(ingredientes)==0:
        print("** - No hay ningún extra\n")
        print(f"""
######################### NOTA ##################
PIZZA
{ingredientes[0]} ........ {gastos[0]}€

                                            TOTAL
                                            {sum(gastos)}€
                                            PAGADO
                                            {dinero_usuario}€
                                            CAMBIO
                                            {(dinero_usuario)-sum(gastos)}€
###################################################
        """)
    else:
        print(f"""
######################### NOTA ###################
PIZZA""")
        i=0
        for  i in range(len(ingredientes)):
            print(f"{ingredientes[i]} ...... {gastos[i]}€")
            i=i+1
        print(f"""
                                            TOTAL
                                            {sum(gastos)}€
                                            PAGADO
                                            {dinero_usuario}€
                                            CAMBIO
                                            {(dinero_usuario)-sum(gastos)}€
###################################################
        """)
        
   
   
# Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos. No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el pedido.
# Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes (piensa que los precios son los que son y no deben variar en todo el programa).
# Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el cambio que le queda.
# Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
# Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total gastado, el cambio y todos los elementos que se han añadido al pedido, pizza, ingredientes extra y precios.


# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
# El usuario podrá elegir solo una pizza.
#Esto lo hago así con variables para el precio y el nombre según se eliga pero lo podría haber hecho con una tupla:
#y quedaría así  pizza_margarita=("Margariata", 10)







