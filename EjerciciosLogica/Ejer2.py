#Dada una palabra , buscarla en una frase y devolver cuantas veces aparece
#La frase y la palabra deben ser parametros de una funcion
#Ejercicio Realizado por Victor Rubio 23 Oct 2023
def count_str(phrase,char):
    count = 0
    sep = phrase.split()
    for i in sep:
        if i == char:
            count +=1
    return count 
    


phrase= "Hola soy un a frase con la palabra, palabra"
char = "palabra"



resul = count_str(phrase, char)

print( f"La palabra {char} aparece {resul} veces en la frase")

phrase = "Hola mi nombre es cadena, victor"
char ="victor"
resul = count_str(phrase, char)
print(f"La palabra {char} aparece {resul} veces en la frase")