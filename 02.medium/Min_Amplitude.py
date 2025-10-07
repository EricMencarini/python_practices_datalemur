#https://datalemur.com/questions/python-min-amplitude

'''
Given an integer array arr, the difference between the largest and smallest values is 
called amplitude. If you can change up to three elements of the array to any value, 
return the minimum possible amplitude.
'''
arr = [4, -8, -1, 3, 7, 10, 5]


def min_amplitude(arr):
	
	arr.sort()
	
	n = len(arr)

	if n <= 4:
		return 0
	arr1 = arr[n-1] - arr[3]
	print(arr1)
	arr2 = arr[n-2] - arr[2]
	print(arr2)
	arr3 = arr[n-3] - arr[1]
	print(arr3)
	arr4 = arr[n-4] - arr[0]
	print(arr4)

	return min(arr1,arr2,arr3,arr4)

print(min_amplitude(arr))