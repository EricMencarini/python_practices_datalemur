#https://datalemur.com/questions/python-factorial-formula

'''
Given a number n, write a formula that returns n!.

In case you forgot the factorial formula n! = n * (n-1) * (n-2) * 2 * 1

For example, 5! = 5*4*3*2*1 = 120 so we'd return 120.

p.s. if this problem seems too trivial, try the follow-up 
Microsoft interview problem Factorial Trailing Zeroes

'''
def fatorial(n):
    z = 1
    x = n
    while x >= 1: 
       z *= x
       x -= 1
    return z 
