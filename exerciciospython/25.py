"""
imposto = float(input('insira o valor do imposto'))
salario = int(input('insiraa o valor do salario'))

print("valor real: {0}".format(salario - (salario *( imposto * 0.01))))

"""

"""
imposto = (input('insir o valor do imposto'))
salario = int(input('insira o valor do salario'))

if not imposto:
	imposto = 27.5
else: 
	float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

"""

imposto = float(input("insira o valor do imposto:"))

if imposto < 10:
	print("baixo")

if imposto >= 10 and imposto  <= 27.5:
	print("ok")
else:
	print("imposto invalido")



