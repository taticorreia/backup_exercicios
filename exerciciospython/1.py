a = int(input('valor de a:'))
b = int(input('Valor de b:'))
c = int(input('valor de c:'))
d = int(input('valor de d:'))

"""
if (a>b) and (a>c) and (a>d):
	print("o maior numero e {0}".format(a))
elif (b>a) and (b>c) and (b>d):
	print("o maior numer e {0}".format(b))
elif (c>a) and (c>b) and (c>d):
	print("o maior numero e {0}".format(c))
elif (d>a) and (d>b) and (d>c): 
	print("o maior numero e {0}".format(d))
else:
	print('todos sao iguais')
"""

m = a

if b > m:
	m = b

if c > m:
	m = c

if d > m:
	m = d

print('O maior numero e: %d' % (m))



