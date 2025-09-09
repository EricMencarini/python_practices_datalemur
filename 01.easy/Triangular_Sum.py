#https://datalemur.com/questions/python-triangular-sum-of-an-array

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
