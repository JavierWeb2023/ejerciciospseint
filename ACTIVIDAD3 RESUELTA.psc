Algoritmo ACTIVIDAD3
	// Se le pedir� al usuario ingresar 5 n�meros enteros de los cuales se tendr� que mostrar en pantalla si los mismos son par o impar.
	// Ejemplo:
	// El usuario ingresa el valor 3, inmediatamente se tendr� que mostrar "es impar". Luego ingresa 10, se tendr� que mostrar "es par".
	
	Definir contador, limite, dato Como Entero;
	
	limite <- 5;
	
	Para contador<-1 Hasta limite Hacer
		Escribir 'Ingresar n�mero';
		Leer dato;
		
		Si((dato % 2)==0) Entonces
			Escribir 'El n�mero es par';
		SiNo
			Escribir 'El n�mero es impar';
		FinSi
	FinPara

FinAlgoritmo
