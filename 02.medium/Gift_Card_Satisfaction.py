#https://datalemur.com/questions/python-gift-card-satisfaction

expectations = [5, 20, 1000]
cards = [10, 15, 100]

def max_satisfaction(expectations, cards):
	e = sorted(expectations)
	c = sorted(cards)
	
	i = 0
	j = 0
	max_satisfy = 0
	
	y = len(c)

	while i < len(e) and j < len(c): 
		if e[i] <= c[j]:
			max_satisfy += 1
			i += 1
			j += 1
		else:
			j += 1
		 

	return max_satisfy

print(max_satisfaction(expectations, cards))