# Ingresar el sueldo de una persona, si supera los 80000000 millones mostrar un 
# mensaje en pantalla indicando que debe abonar IRP.
# Si no, mostrar el mensaje "La persona no debe abonar impuestos".

MONTO_IRP = 80000000
sueldo = int(input("Ingrese cuál es su sueldo: "))

sueldo_anual = sueldo * 12  # Calcular por los 12 meses
if sueldo_anual > MONTO_IRP:
    print("Esta persona debe pagar impuestos")
else:
    print("La persona no debe abonar impuestos")
