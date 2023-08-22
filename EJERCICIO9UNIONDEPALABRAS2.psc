Algoritmo EJERCICIO9UNIONDEPALABRAS2
	// Crear un programa que una dos palabras ingresadas por teclado
	// invirtiendo su orden cuando la segunda tenga más letras que la
	// primera o lo deje igual si la primera es más larga que la segunda.
	
	Definir palabra1, palabra2, combinacion1, combinacion2 Como Cadena
	
	Escribir 'Ingrese una palabra'
	Leer palabra1
	
	Escribir 'Ingrese otra palabra'
	Leer palabra2
	
	combinacion1 <- Concatenar(palabra1,palabra2)
	combinacion2 <- Concatenar(palabra2,palabra1)
	
	Si Longitud(palabra2)>Longitud(palabra1) Entonces
		Escribir combinacion2
	SiNo
		Escribir combinacion1
	FinSi
	
FinAlgoritmo
