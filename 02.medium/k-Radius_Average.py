#https://datalemur.com/questions/python-k-radius-average

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