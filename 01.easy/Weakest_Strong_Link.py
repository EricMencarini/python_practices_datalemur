#https://datalemur.com/questions/python-weakest-strong-link

'''
You know that phrase, how a chain is only as strong as its weakest link?

Imagine you had a chain-link fence, represented as a matrix. For the chain-link at 
position (i, j), the input matrix strength[i][j] indicates how strong the chain is 
at that position (where stronger means a higher number). The numbers in the matrix 
are unique.

The Weakest Strong Link is defined as the weakest chain-link in its row but also the 
strongest link in its column.

Given a matrix strength, return the weakest strong link if it exists; otherwise, 
return -1. If a weakest strong link exists, it is always exactly one, and it can be 
proven that no other link will satisfy both conditions simultaneously.

'''
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