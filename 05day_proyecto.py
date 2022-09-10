###############################################################
########################## PROYECTO ###########################
# El proyecto va a ser un pequeño programa de consola que permita al usuario hacer un pedido de pizza con ingredientes extra para añadir.

# Requisitos del proyecto
# Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
print("-> Pizzería PF <-")

# El usuario introducirá el dinero que quiera. Guárdalo en una variable.
saldo_usuario=float(input("Cuanto dinero tienes?: "))

# Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
ingredientes=["Carne", "Salsa Barbacoa", "Peperoni", "Roquefort", "Anchoas", "Pimientos", "Cebolla", "Chorizo"]
ingredientes_seleccionados=[]

# Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
# Cada pizza tendrá un coste diferente.
pizza_margarita=("Margarita", 10)
pizza_mediterranea=("Medriterránea",14)
pizza_cuatro_quesos=("4 Quesos", 16)
print(f""" Lista de Precios
    Pizza Margarita {pizza_margarita}€
    Pizza Mediterránea {pizza_mediterranea}€
    Pizza 4 Quesos {pizza_cuatro_quesos}€""")

# El usuario podrá elegir solo una pizza.
elige_pizza=int (input("Por favor elige una de las pizas (1-Margarita / 2-Mediterránea / 3-Cuatro Quesos): "))

# Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
coste_actual=0
if elige_pizza == 1:
    coste_actual=pizza_margarita[1]
    print(f"Llevas gastado {coste_actual}€")
if elige_pizza == 2:
    coste_actual=pizza_mediterranea[1]
    print(f"Llevas gastado {coste_actual}€")
if elige_pizza == 3:
    coste_actual=pizza_cuatro_quesos[1]
    print(f"Llevas gastado {coste_actual}€")

# Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
anadir_extras=False
pregunta_extras=input("Deseas añadir ingredientes extras? ")
if pregunta_extras.lower() == "si":
    anadir_extras=True
if pregunta_extras.lower() == "no":
    anadir_extras=False

if anadir_extras==False:
    print(f"El precio de su pedido es de: {coste_actual}")    
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


