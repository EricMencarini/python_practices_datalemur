#https://datalemur.com/questions/python-coin-change

'''
Explanation:
There are several combinations to make up the amount 5, such as:

using five 1's (1 + 1 + 1 + 1 + 1)
using three 1's and one 2 (1 + 1 + 1 + 2)
using two 2's and one 1 (2 + 2 + 1)
using one 4 and one 1 (4 + 1)
The combination that uses the fewest coins is the last one (using 4 and 1), which totals 2 coins.
'''
coins = [2, 4, 1, 4]
target_amount = 5
#Output: 2

def coin_change(coins, target_amount):
	unique = set(coins)
	i = 0 
	while i < len(unique):
		j = 0
		while j < len(unique):
			if coins[i] == target_amount or coins[i] + coins[j] == target_amount:
				return 1
			j += 1
		i += 1
	return -1

print(coin_change(coins,target_amount))