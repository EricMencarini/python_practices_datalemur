#https://datalemur.com/questions/python-base-13-conversion
num = 125

'''
Given an integer num, return its string representation in base 13.

In case you don’t use base 13 that much (who does, right?), here’s a quick rundown: 
just like base 10 uses digits from 0 to 9. But also for 10, 11 and 12, 
we use the letters A, B, and C.

For example:
'''
def convertToBase13(num):
    map_13 = ['0','1','2','3','4','5','6','7','8','9','A','B','C']
    
    if num == 0:
        return map_13[0]
        
    if num < 0:
        return '-' + convertToBase13(-num)

    if num < 13:
        return map_13[num]

    return convertToBase13(num // 13) + map_13[num % 13]


print(convertToBase13(num))