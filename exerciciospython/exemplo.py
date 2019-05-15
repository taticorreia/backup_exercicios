salario = int(input('Salario?'))
imposto = float(input('imposto em 27.5'))


if not imposto:
	imposto = 27.5
else:
	imposto = float(imposto)
	print("valor real: {0}".format(salario - (salario * 0.5 * 0.01)))




