#PROGRAMA PARA PRACTICAR PROGRAMACIÓN ORIENTADA A OBJETOS
#ANIMALES


class Animales():
    def __init__(self,nombre):
        self.nombre=nombre

    def hacer_sonido(self):
        pass

    def mostrar_informacion(self):
        print("Nombre:",self.nombre)

class Perro(Animales):
    def __init__(self, nombre, raza):
        super().__init__(nombre) #llamando al constructor de la clase padre y pas
        self.raza=raza

    def hacer_sonido(self):
        print("Ladrido")

    def mostrar_informacion(self):
        return super().mostrar_informacion()
        print("Raza", self.raza)


class Gato(Animales):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color=color

    def hacer_sonido(self):
        print("Maullando")

    def mostrar_informacion(self):
        return super().mostrar_informacion()
        print("color",self.color)


perro1=Perro("Max","Labrador")
gato1=Gato("Luna","Blanco")

perro1.hacer_sonido()
perro1.mostrar_informacion()


gato1.hacer_sonido()
gato1.mostrar_informacion()