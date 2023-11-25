#Dada una cadena de texto, darle la vuelta e invertir el orden
#de sus caracteres, sin usar metodos propios del lenguaje
#solo estructuras de control
def inver_char(str):
    inv = ""
    for i in range (len(str)-1,-1,-1):
        inv += str[i]
    return inv

print("Palabras a invertir: victor, sabritas, perro")
print(inver_char(str="victor"))
print(inver_char(str="sabritas"))
print(inver_char(str="perro"))