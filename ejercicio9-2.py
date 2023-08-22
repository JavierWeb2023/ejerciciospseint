# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Crear un programa que una dos palabras ingresadas por teclado
	# invirtiendo su orden cuando la segunda tenga más letras que la
	# primera o lo deje igual si la primera es más larga que la segunda.
	palabra1 = str()
	palabra2 = str()
	combinacion1 = str()
	combinacion2 = str()
	print("Ingrese una palabra")
	palabra1 = input()
	print("Ingrese otra palabra")
	palabra2 = input()
	combinacion1 = palabra1+palabra2
	combinacion2 = palabra2+palabra1
	if len(palabra2)>len(palabra1):
		print(combinacion2)
	else:
		print(combinacion1)

