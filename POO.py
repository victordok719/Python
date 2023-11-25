class Motor:
    def iniciar(self):
        print("Motor encendido")

class CajaVelocidad:
    def cambiar_marcha(self, subir=False):
        if subir:
            print("Cambio de marcha hacia arriba")
        else:
            ("Cambio de marcha hacia abajo")

class Carro:
    def __init__(self):
        self.motor=Motor()
        self.velocidades=CajaVelocidad()

    def iniciar_motor(self):
        self.motor.iniciar()
    def cambio_velocidad(self, subir=False):
        self.velocidades.cambiar_marcha(subir)


mi_coche=Carro()
mi_coche.iniciar_motor()
mi_coche.cambio_velocidad(True)
        
