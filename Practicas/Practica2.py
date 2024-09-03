Acceso = {"admin":"123", "Admin":"password", "ADMIN":"Mondongo"}

Usuario = input("Ingrese su Usuario: ")
Contraseña = input("Ingrese su Contraseña: ")

if Usuario in Acceso:
    if Acceso[Usuario] == Contraseña:
        print("Acceso Correcto")
    else:
        i = 1
        while i < 3:
            print("Contraseña incorrecta")
            #Volver Contraseña. 3 Intentos
            print(f"Le quedan {3 - i} intentos")
            
            Contraseña = input("Ingrese su Contraseña: ")
            if Acceso[Usuario] == Contraseña:
                print("Acceso Correcto")
                break
            else:
                i += 1
        if i >= 3 :
            print("Ya no hay intentos cuenta bloqueada")

else:
    print("El usuario no esta registrado")
