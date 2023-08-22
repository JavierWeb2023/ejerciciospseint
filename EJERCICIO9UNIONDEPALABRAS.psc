Algoritmo EJERCICIO9UNIONDEPALABRAS
	// Crear un programa que una dos palabras ingresadas por teclado
	// invirtiendo su orden cuando la segunda tenga más letras que la
	// primera o lo deje igual si la primera es más larga que la segunda.
	
	Definir palabra1, palabra2 Como Cadena
	
	Escribir 'Ingrese una palabra'
	Leer palabra1
	
	Escribir 'Ingrese otra palabra'
	Leer palabra2
	
	Si Longitud(palabra2)>Longitud(palabra1) Entonces
		Escribir palabra2, ' ', palabra1
	SiNo
		Escribir palabra1, ' ', palabra2
	FinSi
	
FinAlgoritmo
