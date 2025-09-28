#https://datalemur.com/questions/python-average-subarray

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