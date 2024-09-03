# traductor
diccionario = {"hola":"hello", "chau":"bye", "perro":"dog"}

while True:
    palabra = input("Ingrese la palabra a traducir: ")

    if(palabra in diccionario):
        print("Español : Ingles")
        print(f"{palabra} : {diccionario[palabra]}")

    else:
        print("La palabra no existe en el diccionario")
        resp = input("Desea registrarlo? (si/no). Salir(x)")
        if resp == "si" or resp == "yes" or resp == "Si" or resp == "Yes":
            #registrar respuesta
            traduccion = input("Ingrese la traducción de esa palabra: ")
            if traduccion != "":
                diccionario[palabra] = traduccion
        else:
            resp == "no" or resp == "No"
            break
        