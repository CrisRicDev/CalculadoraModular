from Operaciones import Suma, Resta, Multiplicacion, Division, Potencia, DivisionEnt 
import questionary

try:
    print("|-----------------------------------|")
    print("    Bienvenido a la calculadora")
    print("|-----------------------------------|")

    a = int(input("Ingrese el primer numero: "))
    operador = questionary.select("Que operacion desea realizar?", choices=["+", "-", "*", "/", "^", "//"]).ask()
    b = int(input("Ingrese el segundo numero: "))

    if operador == "+":
        print("El resultado de la suma es: ", Suma(a, b))
    elif operador == "-":
        print("El resultado de la resta es: ", Resta(a, b))
    elif operador == "*":
        print("El resultado de la multiplicacion es: ", Multiplicacion(a, b))
    elif operador == "/":
        print("El resultado de la division es: ", Division(a, b))
    elif operador == "^":
        print("El resultado de la potencia es: ", Potencia(a, b))
    elif operador == "//":
        print("El resultado de la division entera es: ", DivisionEnt(a, b))
    else:
        print("Operacion no valida")
except ValueError:
    print("Datos no validos")