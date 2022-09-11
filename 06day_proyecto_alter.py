# Requisitos opcionales
#  (-) Te dejo un par de requisitos opcionales por si quieres practicar 
#      un poco más.
#       (x) Crea un programa alternativo que no deje elegir la opción de 
#           operación al usuario. Que le pida infinitamente 2 números 
#           para realizar de golpe las 6 operaciones y vuelta a empezar.



def sumar(num1,num2):
    return num1+num2

def restar(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    return num1/num2

def modulo(num1,num2):
    return num1%num2

def exponente(num1,num2):
    return num1**num2



while True:
    num1=float(input("Escriba el primer numero\n"))
    num2=float(input("Escriba el segundo numero\n"))
    suma=sumar(num1,num2)
    resta=restar(num1,num2)
    multiplicacion=multiplicar(num1,num2)
    division=dividir(num1,num2)
    modular=modulo(num1,num2)
    exponencial=exponente(num1,num2)
    print(f"""
    {suma}
    {resta}
    {multiplicacion}
    {division}
    {modular}
    {exponencial}
    """)

    
   