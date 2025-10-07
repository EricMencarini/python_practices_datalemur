#https://datalemur.com/questions/python-average-subarray

'''
You are given an integer array nums consisting of n elements, and an integer k.

Your task is to find a contiguous subarray of nums whose length is exactly k 
that has the highest average value. 
A subarray is simply a sequence of consecutive elements from the original array. 
After identifying this subarray, return the average value, rounded to two decimal places.
'''
#nums = [1, 2, -5, -3, 10, 3]
#k = 9

def max_avg_subarray(nums,k):
    pos = 0
    avg = None 

    while len(nums) >= pos + k:
        total = sum(nums[pos:pos+k])
        current_avg = total / k

        if avg is None or current_avg > avg:
            avg = current_avg  
        
        pos += 1

    return round(avg,2)