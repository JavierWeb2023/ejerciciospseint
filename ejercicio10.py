# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Crear un programa que ingrese tres números y nos diga si la
	# multiplicación entre los dos primeros es igual al tercer número.
	num1 = int()
	num2 = int()
	num3 = int()
	print("Ingrese primer número")
	num1 = int(input())
	print("Ingrese segundo número")
	num2 = int(input())
	print("Ingrese tercer número")
	num3 = int(input())
	if (num1*num2==num3):
		print("La multiplicación de los dos primeros es igual al tercero ",num1,"*",num2,"=",num3)
	else:
		print("La multiplicación de los dos primeros no es igual al tercero")

