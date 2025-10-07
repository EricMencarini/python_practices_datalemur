#https://datalemur.com/questions/python-hill-climbing

'''
You're attempting to climb a hill—not in a mathematical optimization sense 
(check out hill climbing for that), but literally outside, touching grass, and 
trying to climb a hill.

Imagine there are n steps carved into the hill. You can go up using either 1 or 
2 steps at a time.

Your task is to return the number of distinct ways to reach the top of the hill.
'''

def climb_hill(n):
    if n <= 1:
     return 1
    one_step,two_steps = 1,1
    for _ in range(2 , n+1):
        one_step,two_steps = two_steps, one_step + two_steps
    return two_steps