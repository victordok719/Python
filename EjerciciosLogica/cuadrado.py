#Ejercicio realizado por Victor Rubio 23 oct 2023
#Dibujar un cuadrado hueco con asteriscos

def dibujar_cuadrado(n):
    for i in range (n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end =" ")
            else:
                print(" ", end =" ")
        print()

# Cambia el valor de n al tamaño del cuadrado que desees
n = 4
dibujar_cuadrado(n)