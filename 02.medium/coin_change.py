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
#Solution 1:
def coin_change(coins, target_amount):
    coins_min = [float('inf')] * (target_amount + 1)
    coins_min[0] = 0

    for coin in coins:
        for amount in range(coin, target_amount + 1):
            coins_min[amount] = min(coins_min[amount], coins_min[amount - coin] + 1)

    return coins_min[target_amount] if coins_min[target_amount] != float('inf') else -1

#Solution2:
def coin_change(coins, target_amount):
    unique = list(set(coins))
    min_coins = float('inf')

    amounts = [(0, 0)]  # (soma_atual, quantidade_de_moedas)

    while len(amounts) > 0:
        total, used = amounts.pop(0)
        if total == target_amount:
            if used < min_coins:
                min_coins = used
            continue
        if total > target_amount or used >= min_coins:
            continue

        i = 0
        while i < len(unique):
            amounts.append((total + unique[i], used + 1))
            i += 1

    return min_coins if min_coins != float('inf') else -1
