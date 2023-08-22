# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# En una fábrica de computadoras se planea ofrecer a los clientes un descuento que 
	# dependerá del número de computadoras que compre. Si las computadoras son menos de 
	# cinco se les dará un 10 MOD  de descuento sobre el total de la compra; si el número de 
	# computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20 MOD  de descuento; 
	# y si son 10 o más se les da un 40 MOD  de descuento. El precio de cada computadora es de $11,000
	computadoras = int()
	descuento = int()
	total = int()
	print("Cantidad de computadoras")
	computadoras = int(input())
	total = computadoras*11000
	if (computadoras>0 and computadoras<5):
		descuento = total*0.10
		print("Valor total")
		print((total-descuento))
	else:
		if (computadoras>=5 and computadoras<10):
			descuento = total*0.20
			print("Valor total")
			print((total-descuento))
		else:
			if (computadoras>=10):
				descuento = total*0.40
				print("Valor total")
				print((total-descuento))
			else:
				print("ERROR NÚMEROS NEGATIVOS")

