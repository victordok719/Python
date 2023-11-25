        /*Dada una palabra, crear una función para buscarla en una frase y devolver cuantas veces aparece.
        La frase y la palabra deben ser parámetros de una función.

        Ejemplos:
        coincidencias("hola soy una palabra en una frase", "palabra") debe devolver un 1
        coincidencias("hola soy Javier", "Mario") debe devolver un 0.

        Nota. La salida de la función debe ser en consola
        Nota. No tomar en cuenta mayusculas y minúsculas.
        Nota. No se deben utilizar funciones propias del lenguaje que tengan esta funcionalidad.
        Se recomienda certificar el funcionamiento en replit.com*/

        //Escrito en lenguaje JavaScript, para poder probarlo cambiar la extenseion ya que el formulario no me dejo subir el 

        function busquedaPalabra(frase, palabra) { //funcion para buscar cuantas veces aparece una palabra en una frase
            const palabras = frase.split(' ');//separa la frase
            let contador = 0; //iniciamos contador
            for (let i = 0; i < palabras.length; i++) { //se recorre el tamaño de la frase
              if (palabras[i] === palabra) { //se realiza una comparacion para caber si palabras y palabra son del mismo tipo y valor
                contador++; // incrementa el contador en 1
              }
            }
            return contador; // regresa el contador de las palabras en la frase
          }
        
        const frase = 'hola soy una palabra en una frase';
        const palabra = 'palabra';
        const contador = busquedaPalabra(frase, palabra);
        console.log(`La palabra "${palabra}" aparece ${contador} veces en la frase "${frase}"`); //muestra las veces que aparece la palabra en la frase

