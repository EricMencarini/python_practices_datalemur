#https://datalemur.com/questions/python-most-popular-integers

'''
Given an integer array and an integer n as input, return the top n integers in the 
array (the ones that appear most frequently). 
Return the output in non-decreasing order. 
The test cases are generated in such a way that there will be a unique answer.
'''
nums = [2, 1, 2, 3, 2, 1, 2, 1, 3, 4] 
n = 3

def most_popular(nums,n):
    count_nums = {}
    for element in nums:
        if element not in count_nums:
            count_nums[element] = 1
        else:
            count_nums[element] += 1
    rank = sorted(count_nums, key=count_nums.get, reverse=True)
    rank_n = sorted(list(rank[:n]))
    return rank_n

print(most_popular(nums,n))