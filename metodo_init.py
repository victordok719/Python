class Usuario:
    
    def __init__(self):
        self.usuario="" #se inician los atributos
        self.ingresos=0

    def intro(self): #ingreso de los datos para los atributos
        self.usuario=input("Ingrese el nombre del usuario:")
        self.ingresos=float(input("Cantidad de ingresos anual:"))

    def visualizar(self):
        print("Nombre:",self.usuario)
        print("Ingresos:",self.ingresos)

    def fiscalidad(self):
        if self.ingresos>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


usuario=Usuario()
usuario.intro()
usuario.visualizar()
usuario.fiscalidad()