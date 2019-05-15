i = 0
vetor = []
while i < 10:
	num = int(input('Informe um numero: '))
	vetor.append(num)
	i = i + 1

vetor_ordenado = sorted(vetor)
print('Numeros ordenados: ', vetor_ordenado)

