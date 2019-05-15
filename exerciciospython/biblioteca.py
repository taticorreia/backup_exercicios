def equacao(a, b, c):
    
    from math import sqrt
    
    delta = (b*b) - (4 * a * c)
   
    if delta > 0:
    x1 = (-b + sqrt(delta)) / (2 * a)
    
    