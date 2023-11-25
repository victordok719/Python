#Ejercicio 4
#Obtener el precio final si se le resta el 36% a la cantidad total de la compra

precio = float(input("Ingresa el total de la compra: $"))
descuento = precio * 0.36


precio_final = precio - descuento


print(f"El precio final de la compra es: ${precio_final:.2f}")