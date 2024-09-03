while True:
    notas = []
    valido = True

    for x in range(3):
        while True:
                nota = float(input(f"Ingrese la nota {x+1} (máximo 5): "))
                if 0 <= nota <= 5:
                    notas.append(nota)
                    break 
                else:
                    print("Nota inválida. Debe ser entre 0 y 5.")
                

    if len(notas) == 3: 
        promedio = sum(notas) / len(notas)
        print(f"El promedio es: {promedio:.2f}")

        if promedio <= 1.7:
            print("El estudiante ha sido reprobado")
        else:
            print("El estudiante ha sido aprobado")
        
        break 
    
