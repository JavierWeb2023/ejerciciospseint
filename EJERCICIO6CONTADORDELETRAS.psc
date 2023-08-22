Algoritmo EJERCICIO6CONTADORDELETRAS
	// Crear un programa que al ingresar dos palabras nos diga cual es la
	// que tiene más letras con la siguiente leyenda: "La más larga es:
	// (palabra ingresada)" , en caso de ser iguales dirá: "Ambas palabras
	// tienen la misma cantidad de letras".
	
	Definir palabra1, palabra2 Como Cadena
	
	Escribir 'Ingrese la primera palabra'
	Leer palabra1
	
	Escribir 'Ingrese la segunda palabra'
	Leer palabra2
	
	Si Longitud(palabra1)>Longitud(palabra2) Entonces
		Escribir 'La más larga es:', ' ', palabra1
	SiNo
		Si Longitud(palabra1)<Longitud(palabra2) Entonces
			Escribir 'La más larga es:', ' ', palabra2
		SiNo
			Escribir 'Ambas palabras tienen la misma cantidad de letras'
		FinSi
	FinSi
	
FinAlgoritmo
