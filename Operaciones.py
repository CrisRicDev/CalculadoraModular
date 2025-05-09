def Suma(a, b):
    try:
        return a + b
    except ValueError:
        print("numero no valido")


def Resta(a, b):
    try:
        return a - b
    except ValueError:
        print("numero no valido")


def Multiplicacion(a, b):
    try:
        return a * b
    except ValueError: 
        print("Datos no validos")
        
def Division(a, b):
    try:
        return a / b
    except ZeroDivisionError: 
        print("No es divisible por 0")
        
    
def Potencia(a, b):
    try:
        return a ** b
    except ValueError: 
        print("Datos no validos")

            
def DivisionEnt(a, b):
    try:
        return a // b
    except ZeroDivisionError: 
        print("No es divisble por 0")
        
