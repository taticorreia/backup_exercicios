a = int(input('insira a:'))
b = int(input('insira b:'))
c = int(input('insira c:'))
d = int(input('insira d:'))
e = int(input('insira e:'))
f = int(input('insira f:'))

m = None
if a > b:
	m = a
	a = b
	b = m

if a > c:
	m = a
	a = c
	c = m

if a > d:
	m = a
	a = d
	d = m 

if a > e:
	m = a
	a = e
	e = m

if a > f:
	m = a
	a = f
	f = m

if b > c: 
	m = b
	b = c
	c = m

if b > d:
	m = b
	b = d
	d = m
	
if b > e: 
	m = b
	b = e
	e = m

if b > f:
	m = b
	b = f
	f = m

if c > d:
	m = c
	c = d
	d = m

if c > e:
	m = c
	c = e
	e = m

if c > f:
	m = c
	c = f
	f = m

if d > e:
	m = d
	d = e
	e = m

if d > f:
	m = d
	d = f
	f = m

if e > f:
	m = e
	e = f
	f = m

print('os numeros sao: %d, %d, %d, %d, %d' % (a, b, c, d, e, f))



