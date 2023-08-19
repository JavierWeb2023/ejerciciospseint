Algoritmo ACTIVIDAD2
	
 //En una fábrica de computadoras se planea ofrecer a los clientes un descuento que 
//dependerá del número de computadoras que compre. Si las computadoras son menos de 
//cinco se les dará un 10% de descuento sobre el total de la compra; si el número de 
//computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20% de descuento; 
//y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $11,000
	Definir computadoras,descuento,total Como Entero;
	
	Escribir "Cantidad de computadoras";
	Leer computadoras;
	
	total<-computadoras*11000;
	
	Si(computadoras > 0 y computadoras < 5) Entonces
		descuento<-total*10/100;
		Escribir "Valor total";
		Escribir (total-descuento);
	SiNo
		Si(computadoras >= 5 y computadoras < 10) Entonces
			descuento<-total*20/100;
			Escribir "Valor total";
			Escribir (total-descuento);
		SiNo
			Si(computadoras >= 10) Entonces
				descuento<-total*40/100;
				Escribir "Valor total";
				Escribir (total-descuento);
			SiNo
				Escribir "ERROR NÚMEROS NEGATIVOS";
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
