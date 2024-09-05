# Contar las vocales de una cadena
cadena = input("Ingrese una oracion: ")
vocales = 0

for i in range(0,len(cadena)):
    if(cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u"):
        vocales += 1

print("La cantidad de vocales es:", vocales)
