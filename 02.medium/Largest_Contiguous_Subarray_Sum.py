#https://datalemur.com/questions/python-largest-contiguous-subarray-sum

'''
Given an integer array, find the sum of the largest contiguous subarray within the array.

For example, if the input is [-1, -3, 5, -4, 3, -6, 9, 2], 
then return 11 (because of [9, 2]).

Note that if all the elements are negative, you should return 0.

p.s. this is the same as question 9.5 in Ace the Data Science Interview.
'''

input = [-1, -3, 5, -4, 3, -6, 9, 2]

def max_subarray_sum(input):
    storage_value = 0
    i = 0
    while i < (len(input)):
        j = i
        current_value = 0
        while j < len(input):
            current_value += input[j]
            if current_value > storage_value:
                storage_value = current_value
            j += 1
        i += 1    
    return storage_value


print(max_subarray_sum(input))