# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input("coloque seu peso: "))
altura = float(input("agora coloque sua altura: "))
imc = (peso/altura**2)
if imc < 18.5:
	print ("abaixo do peso")
else:
		if imc >= 18.5 and imc <25:
			print ("peso normal")
if imc >= 25 and imc < 30:
	print ("sobrepeso")
else:
	if imc >= 30:
		print ("obesidade")







