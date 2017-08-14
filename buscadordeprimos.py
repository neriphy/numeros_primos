#Encontrar numeros primos
#Creado por @neriphy

limite = int(input("Defina un limite"))
numero = 3
residuo = True

print(2)

while limite >= numero:
	divisor = numero - 1
	residuo = True
	while divisor > 1 and residuo == True:
		if numero%divisor != 0:
			divisor = divisor - 1
			residuo = True
			if divisor == 1:
				print(numero)
				residuo == False
				numero = numero + 1
		
		elif numero%divisor == 0:
			residuo = False
			numero = numero + 1
