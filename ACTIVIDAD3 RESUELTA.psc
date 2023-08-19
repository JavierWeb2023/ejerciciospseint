Algoritmo ACTIVIDAD3
	// Se le pedirá al usuario ingresar 5 números enteros de los cuales se tendrá que mostrar en pantalla si los mismos son par o impar.
	// Ejemplo:
	// El usuario ingresa el valor 3, inmediatamente se tendrá que mostrar "es impar". Luego ingresa 10, se tendrá que mostrar "es par".
	
	Definir contador, limite, dato Como Entero;
	
	limite <- 5;
	
	Para contador<-1 Hasta limite Hacer
		Escribir 'Ingresar número';
		Leer dato;
		
		Si((dato % 2)==0) Entonces
			Escribir 'El número es par';
		SiNo
			Escribir 'El número es impar';
		FinSi
	FinPara

FinAlgoritmo
