# Leer por teclado dos números e imprimir el mayor o si ambos son iguales.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("Los números ingresados fueron: num1 =", num1, ", num2 =", num2)

if num1 > num2:
    print("El número mayor es:", num1)
elif num1 < num2:
    print("El número mayor es:", num2)
else:
    print("Ambos números son iguales")
