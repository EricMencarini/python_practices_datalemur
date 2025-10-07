#https://datalemur.com/questions/python-looping-number

'''
Given an integer n, check if it is a looping number. 
A looping number has the following properties:

It is repeatedly replaced by the sum of the squares of its digits.
This process continues until:

The number becomes 1, in which case it is not a looping number.

The number starts repeating in a cycle that does not include 1, 
making it a looping number.
Return True if n is a looping number, otherwise return False.
'''


'''
Define if the n is a looping number
'''
def is_looping(n):
    l = [int(digit) for digit in str(n)]
    l = [x**2 for x in l]
    n = sum(l)
    count = 0

    while n != 1 and count < 10:
        l = [int(digit) for digit in str(n)]
        l = [x**2 for x in l]
        n = sum(l)
        count += 1

    if n == 1:
        return False
    if count == 10:
        return True

