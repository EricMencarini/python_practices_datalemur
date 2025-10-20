#https://datalemur.com/questions/python-two-sum-3

'''
Given an array of integers nums and an integer k, 
return the largest possible maxSum < k such that 
maxSum = nums[i] + nums[j] and i ≠ j. If no maxSum < k 
is possible, return -1.

Example #1
Input: nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60
Output: 58
'''

nums = [5,13,25,7,-2,14,22]
k = 21

def two_sum(nums, k):
    storage_value = -1
    i = 0
    while i < len(nums):
        j = 0
        while j < len(nums):
          if i != j and nums[i] + nums[j] < k:
             current_value = nums[i] + nums[j]
             if current_value > storage_value:
                storage_value = current_value
          j += 1
        i += 1    
    return storage_value

print(two_sum(nums,k))