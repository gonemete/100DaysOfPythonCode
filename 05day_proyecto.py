###############################################################
########################## PROYECTO ###########################
# El proyecto va a ser un pequeño programa de consola que permita al usuario hacer un pedido de pizza con ingredientes extra para añadir.

# Requisitos del proyecto
# Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
# El usuario introducirá el dinero que quiera. Guárdalo en una variable.
# Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
# El usuario podrá elegir solo una pizza.
# Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
# Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
# Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos. No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el pedido.
# Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes (piensa que los precios son los que son y no deben variar en todo el programa).
# Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el cambio que le queda.
# Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
# Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total gastado, el cambio y todos los elementos que se han añadido al pedido, pizza, ingredientes extra y precios.

# Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
print("-> Pizzería PF <-")

# El usuario introducirá el dinero que quiera. Guárdalo en una variable.
saldo_usuario=float(input("Cuanto dinero tienes?: "))

# Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
ingredientes=["Carne", "Salsa Barbacoa", "Peperoni", "Roquefort", "Anchoas", "Pimientos", "Cebolla", "Chorizo"]
ingredientes_seleccionados=[]

# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
# El usuario podrá elegir solo una pizza.
#Esto lo hago así con variables para el precio y el nombre según se eliga pero lo podría haber hecho con una tupla:
#y quedaría así  pizza_margarita=("Margariata", 10)
pizza_margarita=10
pizza_mediterranea=14
pizza_cuatro_quesos=16

print(f"""
Bienvenido!
Tenemos las siguientes Pizzas a elegir (Sólo una):
- Pizza Margarita ........ {pizza_margarita}€
- Pizza Mediterránea ..... {pizza_mediterranea}€
- Pizza 4 Quesos ......... {pizza_cuatro_quesos}€
""")
eleccion=int(input("""
Por favor eliga una:
1 - Pizza Margarita
2 - Pizza Mediterránea
3 - Pizza 4 Quesos\n
"""))
elif eleccion<0 or eleccion>4:
    eleccion=int(input("""
Por favor eliga una (marque del 1 al 3):
1 - Pizza Margarita
2 - Pizza Mediterránea
3 - Pizza 4 Quesos\n
"""))

if eleccion == 1:
    print(f"Ha elegido Pizza Margarita\n")
    saldo_actual=saldo_usuario-pizza_margarita
    print(f"Su saldo actual es de: {saldo_actual}€")
elif saldo_actual<0:
    print(f"Su saldo: {saldo_actual}")
    print("No tiene suficiente dinero por favor vuelva a elegir")
    eleccion=int(input("""
Por favor eliga una (marque del 1 al 3):
1 - Pizza Margarita
2 - Pizza Mediterránea
3 - Pizza 4 Quesos\n
"""))
        # break
if eleccion == 2:
    print(f"Ha elegido Pizza Mediterránea\n")
    saldo_actual=saldo_usuario-pizza_mediterranea
    print(f"Su saldo actual es de: {saldo_actual}€")
elif saldo_actual<0:
print(f"Su saldo: {saldo_actual}")
print("No tiene suficiente dinero por favor vuelva a elegir")
eleccion=int(input("""
Por favor eliga una (marque del 1 al 3):
1 - Pizza Margarita
2 - Pizza Mediterránea
3 - Pizza 4 Quesos\n
"""))
        # break
else:
    print(f"Ha elegido Pizza 4 Quesos\n")
    saldo_actual=saldo_usuario-pizza_cuatro_quesos
    print(f"Su saldo actual es de: {saldo_actual}€")
    while saldo_actual<0:
        print(f"Su saldo: {saldo_actual}")
        print("No tiene suficiente dinero por favor vuelva a elegir")
        eleccion=int(input("""
Por favor eliga una (marque del 1 al 3):
1 - Pizza Margarita
2 - Pizza Mediterránea
3 - Pizza 4 Quesos\n
"""))
        # break