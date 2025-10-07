#https://datalemur.com/questions/python-k-radius-average

'''
You're given an array nums of n integers and an integer k.

The k-radius average for a subarray of nums centered at some index i is the average 
of all elements from indices i - k to i + k (inclusive). 
If there aren’t enough elements before or after index i to cover this radius, 
the k-radius average is -1.

Build and return an array averages of length n, where averages[i] contains the 
k-radius average for the subarray centered at index i.

Return your result rounded to 2 decimal places.

p.s. before you tackle this challenge, maybe try this related warmup problem 
from Walmart called Average Subarray (where you find the maximum average of any 
subarray of length k).

'''
nums = [0]
k = 2

def k_radius_avg(nums, k):
  averages = [-1] * len(nums)
  
  k_size = 2 * k + 1
  
  for i in range(len(nums)):
      if i - k >= 0 and i + k < len(nums):
        current_sum = 0
        for j in range(i - k, i + k + 1):
          current_sum += nums[j]
          averages[i] = round(current_sum / k_size, 2)
  return averages

print(k_radius_avg(nums,k))