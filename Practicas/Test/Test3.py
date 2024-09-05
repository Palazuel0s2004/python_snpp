from tkinter import *

class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.dato_campo = StringVar()
        self.ventana.geometry("600x200+100+100")
        self.configurar_interfaz()
        self.tabla = Tabla(self.ventana)

    def configurar_interfaz(self):
        Label(self.ventana, text="Localidad").grid(pady=10, row=0, column=0)
        Entry(self.ventana, textvariable=self.dato_campo, width=50).grid(padx=10, row=0, column=1)
        Button(self.ventana, text="Cargar Localidad", width=20, command=self.cargar_lista).grid(pady=10, row=0, column=2)
        Label(self.ventana, text="Lista de Localidades").grid(pady=10, row=4, column=0)

    def mostrar(self):
        self.ventana.mainloop()

    def cargar_lista(self):
        localidad = self.dato_campo.get().strip()
        if localidad:
            self.tabla.cargar_tabla(localidad)
        else:
            print("No se puede agregar una localidad vacía.")

class Tabla:
    def __init__(self, ventana):
        self.ventana = ventana
        self.tabla = Entry(ventana)
        self.tabla.grid(row=5, column=1)
        self.num_fila = 1

    def cargar_tabla(self, localidad):
        self.tabla = Entry(self.ventana, width=20, fg='black', font=('Arial', 10, 'bold'))
        self.tabla.grid(row=self.num_fila, column=1)
        self.tabla.insert(END, localidad)
        self.num_fila += 1

if __name__ == "__main__":
    ventana_localidad = Ventana()
    ventana_localidad.mostrar()
