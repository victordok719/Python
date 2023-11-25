
def Palindromo(str):
    reversa= "".join(reversed(str))
    return "Es un palindromo" if str==reversa else "No es palindromo"

def esPalindromo(str):
    longuitud=len(str)
    for i in range (longuitud//2):
        if str[i]!=str[longuitud-1-i]:
            return False


    return True


def Palin(str):
    if str == str[::-1]:
        return True
    else:
        return False



str = "otto"
#str="hola"
#str="Victor"
#str="ala"

if Palin(str):
    print(f"El string",{str},"es palíndrome")
else:
    print (f"El string ",{str}, "no es palíndrome.")











print(Palindromo("otto"))
print(Palindromo("hola"))
print(Palindromo("Victor"))
print(Palindromo("ala"))


print(esPalindromo("otto"))
print(esPalindromo("hola"))
print(esPalindromo("Victor"))
print(esPalindromo("ala"))



