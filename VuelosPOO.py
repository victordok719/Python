
import tkinter as tk
from tkinter import Menu, simpledialog

class Vuelos:
    def __init__(self, numero_vuelo, origen, destino,capacidad,asientos_disponibles):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.asientos_disponibles = asientos_disponibles

    def ReservarAsiento(self, num_asientos):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles =-1
            return True
            
            
        else:
            print ("No hay suficientes asientos disponibles para el vuelo")
            return False

    def CancelarReserva(self):
        if self.asientos_disponibles < self.capacidad:
            self.asientos_disponibles += -1
            return True
        else:
            return False

    def MostrarInformacion(self):
        print("Informacion del Vuelo:")
        print("Numero de vuelo: ", self.numero_vuelo)
        print("Origen: ", self.origen)
        print("Destino: ", self.destino)
        print("Capacidad: ",self.capacidad)
        print("Asientos disponibles: ",self.asientos_disponibles)


    def MostrarReseva(self):
        print("Informacion del Vuelo:")
        print("Numero de vuelo: ", self.numero_vuelo)
        print("Origen: ", self.origen)
        print("Destino: ", self.destino)










def realizar_reserva():
    num_asientos = simpledialog.askinteger("Reservar Asientos", "Ingresa el número de asientos que deseas reservar:")
    if num_asientos is not None:  # Comprueba si se ingresó un número
        if miVuelo.ReservarAsiento(num_asientos):
            resultado_label.config(text=f"Se han reservado {num_asientos} asientos.")
            resultado_label.config(text=miVuelo.MostrarReseva())
        else:
            resultado_label.config(text="No hay suficientes asientos disponibles en este vuelo.")

def realizar_cancelacion():
    if miVuelo.CancelarReserva():
        resultado_label.config(text="Cancelación exitosa.")
        
    else:
        resultado_label.config(text="No se pudo cancelar la reserva.")


def acerca_de():
    acerca_de_ventana = tk.Toplevel(ventana)
    acerca_de_ventana.title("Acerca de")
    acerca_de_label = tk.Label(acerca_de_ventana, text="Sistema de Reservas de Vuelos v1.0\nDesarrollado por Victor Rubio")
    acerca_de_label.pack()
    acerca_de_ventana.mainloop()

# Crear una ventana
ventana = tk.Tk()
ventana.title("Sistema de Reservas de Vuelos")

ventana.geometry("800x600")

miVuelo = Vuelos("AV123", "Nueva York", "Los Ángeles", 300,40)


# Menú
menu_bar = Menu(ventana)
ventana.config(menu=menu_bar)

archivo_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Acerca de", command=acerca_de)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

# Etiquetas
info_label = tk.Label(ventana, text=miVuelo.MostrarInformacion())
resultado_label = tk.Label(ventana, text="")

info_label.pack()
resultado_label.pack()

# Botones
reserva_button = tk.Button(ventana, text="Reservar Asiento", command=realizar_reserva)
cancelacion_button = tk.Button(ventana, text="Cancelar Reserva", command=realizar_cancelacion)
salir_button = tk.Button(ventana, text="Salir", command=exit)


reserva_button.pack()
cancelacion_button.pack()
salir_button.pack()

ventana.mainloop()        





        

            

        