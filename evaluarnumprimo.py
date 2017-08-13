#Evaludador de numero primo
#Created by @neriphy

numero = input("Ingrese el numero a evaluar: ")
divisor = numero - 1
residuo = True

while divisor > 1 and residuo == True:
	if numero%divisor != 0:
		divisor = divisor - 1
		print("Evaluando")
		residuo = True 
	
	elif numero%divisor == 0:
		residuo = False


if residuo == True:
	print(numero,"es un numero primo")

if residuo == False:
	print(numero,"no es un numero primo")
