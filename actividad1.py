# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# 1- El profesor comienza ingresando la primera nota del alumno.
	# 2- Luego,ingresa la segunda nota del alumno.
	# 3- Se calcula el promedio de las dos notas ingresadas.
	# 4- Se realiza una verificación para determinar si el promedio es mayor o igual a 70. Si es así, se muestra el mensaje "Promociona".
	# 5- Si el promedio es menor a 70, se realiza otra verificación para determinar si el promedio es mayor o igual a 40. Si es así, se muestra el mensaje "Aprueba".
	# 6- Si el promedio es menor a 40, se muestra el mensaje "Desaprueba".
	nota1 = int()
	nota2 = int()
	promedio = int()
	print("Ingresar nota número 1")
	nota1 = int(input())
	print("Ingresar nota número 2")
	nota2 = int(input())
	promedio = (nota1+nota2)/2
	if (promedio>=70):
		print("Promociona")
	else:
		if (promedio>=40):
			print("Aprueba")
		else:
			print("Desaprueba")

