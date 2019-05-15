fgts = float(input('Valor do fgts:'))


"""
Se o fgts for R$ 7000 o imposto sera de  10%
Se o fgts for R$ 15000 o imposto sera de 15%
"""

if fgts <= 7000:
	print('Valor do fgts: {0}'.format(fgts - (fgts * 0.10)))
else:
	print('Valor do fgts: {0}'.format(fgts - (fgts * 0.15)))


