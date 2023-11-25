/*Determinar si una cadena de caracteres"""
es un palíndromo
Un palíndromo es una palabra o enunciado 
que es escrito de la misma forma de adelante
 y al-revés

Ejemplos:
 -Ejecuto esta función:
 palindromo("otto") // Debe devolver true.
 palindromo("victor") // Debe devolver false.

 Crea una función que regresa verdadero si la 
cadena de texto es un palíndromo.  De otra 
forma, regresa falso.
Nota. La salida de la función debe ser en consola
Se recomienda certificar el funcionamiento en 
replit.com*/

function Palindromo(str) {
    const Reversa = str.split("").reverse().join(""); //se usa split para separar la palabra, reverse para recorrer la palabra
    //y join para unir de nuevo la palabra
    return Reversa === str ? "la palabra es un palindromo" : "la palabra no es un palindromo" //este return devuelve si es un palindromo o no lo es

    
}

console.log(Palindromo("otto"));
console.log(Palindromo("victor"))