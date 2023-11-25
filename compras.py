import mysql.connector


class Producto:
    def __init__(self, id,nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        

class CarritoDeCompras:
    def __init__ (self):
        self.productos = []

    def AgregarProducto(self, producto):
        
        self.productos.append(producto)

    def CalcularTotal(self):
        total = sum(producto.precio for producto in self.productos)
        return total


class Usuario:
    def __init__(self , nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.carrito = CarritoDeCompras()

    def RealizarCompra(self, productos):
        for producto in productos:
            self.carrito.AgregarProducto(producto)
            

        total = self.carrito.CalcularTotal()
        print(f"{self.nombre_usuario} El total de su compra es:  ${total:.2f}")





producto1 = Producto(1, "Camiseta", 20.0)
producto2 = Producto(2, "Pantalón", 35.0)
producto3 = Producto(3, "Zapatos", 50.0)

#Crear carrito de compras
carrito= CarritoDeCompras() 

carrito.AgregarProducto(producto1)
carrito.AgregarProducto(producto2)
carrito.AgregarProducto(producto3)

#Crear usuario
usuario1 = Usuario('Juan') #creacion del objeto usuario con un parametro

#Realizadno compra
print("\n\tREALIZANDO COMPRA DE USUARIO:")


usuario1.RealizarCompra(carrito.productos)



