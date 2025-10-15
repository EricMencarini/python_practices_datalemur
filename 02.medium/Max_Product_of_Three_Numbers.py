#https://datalemur.com/questions/python-maximum-product-three-numbers
'''
Given a list of integers, return the maximum product of any three numbers in the array.
For example, for A = [1, 3, 4, 5], you should return 60, since 
For B = [−4, −2, 3, 5] you should return 40 since 
'''

import numpy as np

#input = [1, 3, 4, 5]
input = [-4, -2, 3, 5]

def max_three(input):
	ordered_input = sorted(input, reverse=True)
	return max(np.prod(ordered_input[:3]), np.prod(ordered_input[-2:] + ordered_input[:1]))

print(max_three(input))

