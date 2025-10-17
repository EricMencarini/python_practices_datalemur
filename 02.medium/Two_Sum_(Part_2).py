#https://datalemur.com/questions/python-two-sum-2

'''
You are given an array of integers nums sorted in non-decreasing order, meaning that each value is equal to or greater than the one before it.

Return the indices of the two values in nums that add up to a given target number.

Clarifications:

There is at most one solution.
If there is no valid solution, return [-1, -1].
Return the indices in increasing order (i.e. [1,3], NOT [3,1]).
Your solution must use constant extra space. 
This means that the size of any objects that you create 
while solving the problem cannot grow with the length of nums. 
As a result, you won't be able to just use your solution from the original Two Sum problem.
'''
nums = [1,3,4,5,7,12,15]
target = 9

def two_sum(nums: list[int], target: int) -> list[int]:
    i = 0
    j = 1
    while i < len(nums):
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return sorted([i, j])
            j += 1
        i += 1
        j = i + 1
    return [-1, -1]

print(two_sum(nums,target))