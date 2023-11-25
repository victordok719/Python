#Dada una cadena de texto, comprobar si es palindromo o no
#Por ejemplo ana, bob, otto, allivessevilla
#Los palindromos son cadenas que se leen igual de izquierda a derecha que de derecha a izquierda
#Ejercicio realizado por Victor Rubio 13 Oct 2023
def palindrome(str):
    #reverse = "".join(reversed(str))
    #return "Es un palindromo" if reverse == str else "No es un palindromo"
    if str == str[::-1]:
        return True
    else:
        return False


str = "otto"
print (palindrome(str))
str = "ana"
print (palindrome(str))
str = "bob"
print(palindrome(str))
str = "allivessevilla"
print(palindrome(str))
str = "victor"
print(palindrome(str))
