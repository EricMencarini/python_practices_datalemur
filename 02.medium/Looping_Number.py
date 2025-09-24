#https://datalemur.com/questions/python-looping-number

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

