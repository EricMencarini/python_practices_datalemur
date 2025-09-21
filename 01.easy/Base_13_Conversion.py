#https://datalemur.com/questions/python-base-13-conversion
num = 125

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