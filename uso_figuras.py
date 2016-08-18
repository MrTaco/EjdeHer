from cuadrado import Cuadrado
from triangulo import Triangulo

continuar=False
while continuar==False:
	opc=int(input("1-Crear Figura \n2-Salir "))
	if opc==1:
		figura=int(input("1-Cuadrado \n2-Triangulo "))
		if figura==1:
			lado=int(input("Lado: "))
			cuadrado=Cuadrado(lado)
			opc2=int(input("1-Calcular el area \n2-Imprimir figura "))
			if opc2==1:
				print ("Area: ", cuadrado.calcular_area())
			elif opc2==2:
				print ("Figura: " )
				print(cuadrado.imprimir())
		if figura==2:
			base=int(input("Base: "))
			altura=int(input("Altura: "))
			triangulo=Triangulo(base,altura)
			opc2=int(input("1-Calcular el area \n2-Imprimir figura "))
			if opc2==1:
				print ("Area: ", triangulo.calcular_area())
			elif opc2==2:
				print ("Figura:" )
				print(triangulo.imprimir())
	else: 
		continuar = True
print("Prceso Terminado")