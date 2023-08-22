# Este codigo ha sido generado por el modulo psexport 20230113-l64 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Se le pedirá al usuario ingresar 5 números enteros de los cuales se tendrá que mostrar en pantalla si los mismos son par o impar.
	# Ejemplo:
	# El usuario ingresa el valor 3, inmediatamente se tendrá que mostrar "es impar". Luego ingresa 10, se tendrá que mostrar "es par".
	contador = int()
	limite = int()
	dato = int()
	limite = 5
	for contador in range(1,limite+1):
		print("Ingresar número")
		dato = int(input())
		if ((dato%2)==0):
			print("El número es par")
		else:
			print("El número es impar")

