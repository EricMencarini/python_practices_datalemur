#https://datalemur.com/questions/python-hill-climbing

def climb_hill(n):
    if n <= 1:
     return 1
    one_step,two_steps = 1,1
    for _ in range(2 , n+1):
        one_step,two_steps = two_steps, one_step + two_steps
    return two_steps