def suma(num1: float, num2: float):
    return num1 + num2
    
def resta(num1: float, num2: float):
    return num1 - num2

def multiplicacion(num1: float, num2: float):
    return num1 * num2

def division(num1: float, num2: float):
    if num2 == 0:
        return "No se puede dividir por 0"
    
    return num1 / num2
