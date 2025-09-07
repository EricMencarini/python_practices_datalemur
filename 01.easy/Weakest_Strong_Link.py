#https://datalemur.com/questions/python-weakest-strong-link

strength = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def weakest_strong_link(strength):
    m = len(strength)
    n = len(strength[0])

    min_r = [0] * m
    max_c = [0] * n


    for i in range(m):
        min_r[i] = min(strength[i])
        
    for j in range(n):
        cur_max = 0
        for i in range(m):
            cur_max = max(cur_max, strength[i][j])
        max_c[j] = cur_max
    for i in range(m):
        for j in range(n):
            if strength[i][j] == min_r[i] and strength[i][j] == max_c[j]:
                return strength[i][j]
    
    return - 1

print(weakest_strong_link(strength))