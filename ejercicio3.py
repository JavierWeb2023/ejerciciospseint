# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	num1 = int()
	num2 = int()
	num3 = int()
	print("Ingrese el primer número")
	num1 = int(input())
	print("Ingrese el segundo número")
	num2 = int(input())
	print("Ingrese el tercer número")
	num3 = int(input())
	if (num1>num2 and num1>num3):
		print("El número mayor es:",num1)
	else:
		if (num2>num1 and num2>num3):
			print("El número mayor es:",num2)
		else:
			print("El número mayor es:",num3)

