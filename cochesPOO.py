#COOCHES CON PROGRAMACION ORIENTADA A OBJETOS


class Coche:
    def __init__(self,marca,modelo,año,color):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.color=color
        self.velocidad=0


    def acelerar(self,incremento):
        self.velocidad+=incremento

    def frenar(self,decremento):
        self.velocidad=decremento

    def mostrar_informacion(self):
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Año:",self.año)
        print("Color:",self.color)
        if (self.velocidad==0):
            print ("Velocidad 0 km/h")
        else :
            print(f"Velocidad actual {self.velocidad},km/h")


mi_coche=Coche("Toyota","Corola",1996,"Rojo")

mi_coche.acelerar(50)
mi_coche.mostrar_informacion()

mi_coche.frenar(0)
mi_coche.mostrar_informacion()