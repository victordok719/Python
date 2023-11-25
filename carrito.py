class Producto():
    def __init__(self,nombre,precio,cantidad):
        self.nombre= nombre
        self.precio = precio
        self.cantidad=cantidad

    def obtenerNombre(self):
        return "El producto es: "+str(self.nombre)

    def obtenerPrecio(self):
        return self.precio

    def cantidadDisponible(self):
        if (int(self.cantidad)>0):
            print ("Hay", int(self.cantidad), "unidades disponibles")
        else :
            print ("No hay unidades en stock.")

class Carrito():
    
    def __init__(self):
        self.__listaProductos=[]

    def agregar_productos(self,producto):
        self.__listaProductos.append(producto)

    def total_compra(self):
        total=0
        for producto in self.__listaProductos:
            total+=producto.obtenerPrecio()
        return total

    def realizar_pago(self):
        total_compra=self.total_compra()
        return print("El total a pagar es",total_compra)

    def mostrar_productos(self):
        for producto in self.__listaProductos:
            print("-"*5,"Producto:",producto.obtenerNombre())



mi_carrito=Carrito()


producto1 = Producto("Camiseta", 20, 5)
producto2 = Producto("Pantalón", 60, 3)

mi_carrito.agregar_productos(producto1)
mi_carrito.agregar_productos(producto2)

mi_carrito.mostrar_productos()


mi_carrito.total_compra()

mi_carrito.realizar_pago()

    

    