Algoritmo ACTIVIDAD1
//	1- El profesor comienza ingresando la primera nota del alumno.
//	2- Luego,ingresa la segunda nota del alumno.
//	3- Se calcula el promedio de las dos notas ingresadas.
//	4- Se realiza una verificación para determinar si el promedio es mayor o igual a 70. Si es así, se muestra el mensaje "Promociona".
//	5- Si el promedio es menor a 70, se realiza otra verificación para determinar si el promedio es mayor o igual a 40. Si es así, se muestra el mensaje "Aprueba".
//	6- Si el promedio es menor a 40, se muestra el mensaje "Desaprueba".
	Definir nota1,nota2,promedio Como Entero;
	Definir meta1,meta2 Como Entero;
	
	meta1<-70;
	meta2<-40;
	
	Escribir "Ingresar nota número 1";
	Leer nota1;
	Escribir "Ingresar nota número 2";
	Leer nota2;
	
	promedio<-(nota1+nota2)/2;
	
	Si(promedio>=meta1) Entonces
		Escribir "Promociona";
	SiNo
		Si(promedio>=meta2) Entonces
			Escribir "Aprueba";
		SiNo
			Escribir "Desaprueba";
		Fin Si
	Fin Si
	
FinAlgoritmo
