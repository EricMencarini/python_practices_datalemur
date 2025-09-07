#https://datalemur.com/questions/python-factorial-formula

def fatorial(n):
    z = 1
    x = n
    while x >= 1: 
       z *= x
       x -= 1
    return z 
