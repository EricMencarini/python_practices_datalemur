'''
Given a list of integers nums, and an integer target, return the indices of the two numbers which sum up to the target. Do not use the same list element twice.

Clarifications:

There is at most one solution.
If there is no valid solution, return [-1, -1].
Return the indices in increasing order (i.e. [1,3], NOT [3,1]).
 nums = [1, 4, 6, 10], target = 10
'''
nums = [1, 4, 6, 10] 
target = 10

def two_sum(nums: list[int], target: int) -> list[int]:
    i = 0
    j = 1
    while i < len(nums):
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return sorted([i,j])
            j += 1
        i += 1
        j = i + 1

print(two_sum(nums, target))