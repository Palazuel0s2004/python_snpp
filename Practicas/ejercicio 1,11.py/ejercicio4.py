import random

while True:
    aleatorio = random.randrange(0, 2)
    elijePc = ""
    print("1. Piedra")
    print("2. Tijera")
    print("3. Papel")
    opcion = int(input("Elije tu opcion "))

    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Tijera"
    elif opcion == 3:
        elijeUsuario = "Papel"
    print("Elejiste: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "Piedra"
    elif aleatorio == 1:
        elijePc = "Tijera"
    elif aleatorio == 2:
        elijePc = "Papel"
    print("La maquina elijio: ", elijePc)
    print("...")
    if elijePc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste, Papel envuelve Piedra")
    elif elijePc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta Papel")
    elif elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste, Piedra machaca Tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("Perdiste, Papel envuelve Piedra")
    elif elijePc == "Tijera" and elijeUsuario == "Papel":
        print("Perdiste, Tijera corta Papel")
    elif elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("Perdiste, Piedra machaca Tijera")
    elif elijePc == elijeUsuario:
        print("Empate, Elijieron lo mismo")