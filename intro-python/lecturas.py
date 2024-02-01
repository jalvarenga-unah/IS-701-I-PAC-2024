def area_triangulo(base: float, altura: float):
    return (base * altura) / 2

try:

    # input (str) -> int ( '3' -> 3 ) ✅
    # input (str) -> int ( 'hola' -> error ) ❌ 
    # input (str) -> float ( '3.5' -> 3.5 ) ✅
    # input (str) -> dict ( '{"nombre":"Juan"}' -> {"nombre":"Juan"} ) ✅

    base   =  float(input('Ingrese la base del triángulo: '))
    altura =  float(input('Ingrese la altura del triángulo: '))
except:
    print('Error: Ingrese un número válido')
    exit() # termina la ejecución del programa

area = area_triangulo( altura = altura, base = base) 
print(f'el área del triángulo es: {area}')


def saludo(nombre: str, apellido:str):
    print(f'Hola {nombre} {apellido}')

saludo(apellido= 'Pérez', nombre= 'Juan')
