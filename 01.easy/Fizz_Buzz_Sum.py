#https://datalemur.com/questions/python-fizz-buzz-sum

'''
Write a function fizz_buzz_sum to find the sum of 
all multiples of 3 or 5 below a target value.

For example, if the target value was 10, the multiples of 3 
or 5 below 10 are 3, 5, 6, and 9.
'''

#%%
'''
find the sum of all multiples of 3 and 5 below a target value
'''
target = 10
def fizz_buzz_sum(target):
  n = 0
  all_multiples = []
  for n in range(n,target,+1):
    if n % 3 == 0 or n % 5 == 0:
      all_multiples.append(n) 

  return sum(all_multiples)

#%%
#solution 2
target = 10
def fizz_buzz_sum(target):
    all_multiples = sum(n for n in range(target) 
                        if n % 3 == 0 or n % 5 == 0)
    return all_multiples


