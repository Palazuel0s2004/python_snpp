# Mostrar los números pares del 1 al 100 usando while y otro con for.

# Usando while
x = 1
while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1

# Usando for
for x in range(1, 101):
    if x % 2 == 0:
        print(x)
