# hacer un entorno grafico con tkinter donde incluya 5 botones de opciones y un boton de salir, ademas de un label que muestre el resultado de la opcion seleccionada. Cada boton imprimira un plot de la opcion seleccionada.
import tkinter as tk


def seleccionar(opcion):
    resultado.set("La opcion seleccionada es: " + opcion)


def salir():
    ventana.destroy()


ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Seleccion de opciones")

resultado = tk.StringVar()

etiqueta = tk.Label(ventana, text="Seleccione una opcion")
etiqueta.pack()

boton1 = tk.Button(ventana, text="Opcion 1", command=lambda: seleccionar("Opcion 1"))
boton1.pack()

boton2 = tk.Button(ventana, text="Opcion 2", command=lambda: seleccionar("Opcion 2"))
boton2.pack()

boton3 = tk.Button(ventana, text="Opcion 3", command=lambda: seleccionar("Opcion 3"))
boton3.pack()

boton4 = tk.Button(ventana, text="Opcion 4", command=lambda: seleccionar("Opcion 4"))
boton4.pack()

boton5 = tk.Button(ventana, text="Opcion 5", command=lambda: seleccionar("Opcion 5"))
boton5.pack()

etiquetaResultado = tk.Label(ventana, textvariable=resultado)
etiquetaResultado.pack()

botonSalir = tk.Button(ventana, text="Salir", command=salir)
botonSalir.pack()

ventana.mainloop()
# fin del programa
