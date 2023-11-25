class Banco():
    def __init__(self,nombre):
        self.nombre=nombre
        self.clientes=[]

    def agregar_cliente(self,cliente):
        self.clientes.append(cliente)

    def realizar_transaccion(self,cliente,monto):
        if cliente in self.clientes:
            cliente.realizar_transaccion(monto)
            print("Transacción realizada exitosamente")
        else:
            raise ValueError('El cliente no está registrado en el banco')

    def mostrar_saldo(self,cliente):
        if cliente in self.clientes:
            cliente.mostrar_saldo()
        else:
            return "Cliente no encontrado"

class Cliente:
    def __init__(self, nombre, cuentaBancaria):
        self.nombre=nombre
        self.saldo=cuentaBancaria

    def realizar_transaccion(self,monto):
        self.saldo+=monto

    def mostrar_saldo(self):
        print("{} tiene un saldo de {}".format(self.nombre,self.saldo))


banco=Banco("Mi banco")


Cliente1=Cliente("Juan",1000)
Cliente2=Cliente("Maria",500)


banco.agregar_cliente(Cliente1)
banco.agregar_cliente(Cliente2)

banco.realizar_transaccion(Cliente1, -500)
banco.mostrar_saldo(Cliente1)


banco.realizar_transaccion(Cliente2,200)
banco.mostrar_saldo(Cliente2)


Cliente3=Cliente("Carlos",200)
banco.agregar_cliente(Cliente3)
banco.mostrar_saldo(Cliente3)
banco.realizar_transaccion(Cliente3,200000)
banco.mostrar_saldo(Cliente3)


