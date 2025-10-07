#https://datalemur.com/questions/python-triangular-sum-of-an-array

'''
You are given an integer array nums, where each element in it is a single digit (0-9).

The triangular sum of nums is the value of the only element present in nums 
after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a 
new integer array newNums of length n - 1.
For each index i, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, 
where % denotes the modulo operator.

Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

'''
nums = [1, 3, 5, 7]
#nums_two = [9, 7, 5, 3]
'''
Return the triangular sum of nums.
'''
def triangular_sum(nums):
    if len(nums) == 1:
        return nums[0]
    
    new_nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
    
    return triangular_sum(new_nums)

print(triangular_sum(nums))  
