# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Crear un programa que al ingresar dos palabras nos diga cual es la
	# que tiene más letras con la siguiente leyenda: "La más larga es:
	# (palabra ingresada)" , en caso de ser iguales dirá: "Ambas palabras
	# tienen la misma cantidad de letras".
	palabra1 = str()
	palabra2 = str()
	print("Ingrese la primera palabra")
	palabra1 = input()
	print("Ingrese la segunda palabra")
	palabra2 = input()
	if len(palabra1)>len(palabra2):
		print("La más larga es:"," ",palabra1)
	else:
		if len(palabra1)<len(palabra2):
			print("La más larga es:"," ",palabra2)
		else:
			print("Ambas palabras tienen la misma cantidad de letras")

