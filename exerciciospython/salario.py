salario = float(input('informe seu salario: '))

"""
Regras de negocio do programa:
1. Salario de ate 10 mil, o imposto calculado e 5%
2. Salario maior que 10 mil o imposto calclado e 10%
"""

if salario <= 10000:
        print('Valor do salario: {0}'.format(salario - (salario * 0.05)))
else:
        print('Valor do salario: {0}'.format(salario - (salario * 0.10)))






	
