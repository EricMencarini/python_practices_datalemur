#n = 3
#n = 4
n = 10

def generate_fractions(n):
    list = []
    
    for num in range(1, n):
        for den in range(num + 1, n + 1):
            is_coprime = True
            for x in range(2, min(num, den) + 1):
                if num % x == 0 and den % x == 0:
                    is_coprime = False
                    break
            if is_coprime:
                list.append([num, den])
    return list