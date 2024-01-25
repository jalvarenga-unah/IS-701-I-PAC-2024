# Operadores: ==, !=, >, <, >=, <=
# Operadores lógicos: and, or, not

# Ejemplo 1
a = 5
b = 10
c = 15

if a > b:
    if a > c:
        print("a es el mayor")
    else:
        print("a es mayor que b")
    print('sigo dentro del if')
else:
    print("a no es mayor que b")
    print('sigo dentro del else')
print('ya sali del if')

# Ejemplo 2

if a > b:
    print("a es mayor que b")
elif a > c:
    print("a es mayor que c")
else:
    print("a no es mayor que b ni c")





