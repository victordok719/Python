"""
Factorial de un numero
function factorial(n):
    si n == 0 entonces
        retornar 1
    sino
        retornar n * factorial(n-1)



Fibonacci
function fibonacci(n):
    si n <= 1 entonces
        retornar n
    sino
        retornar fibonacci(n-1) + fibonacci(n-2)

"""


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("******************************************************************************")
print("FACTORIAL:")
n=int(input("Ingresa el valor del numero que quieres calcular su factorial: "))
print("******************************************************************************")
resultado=factorial(n)
print("******************************************************************************")
print("FACTORIAL:")
print("El resultado de tu numero: ",n, "es", resultado)
print("******************************************************************************")

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


res=fibonacci(n)
print("******************************************************************************")
print("FIBONACCI")
print("La serie de fibonacci para el numero: ", n,"es", res)
print("******************************************************************************")

