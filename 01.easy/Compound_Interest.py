#https://datalemur.com/questions/python-compound-interest

principal = 500
rate = 10
contribution = 50
years = 3

'''
compound interest calculator, using the four variables above as input:
'''
def compound_interest(principal, rate, contribution, years):
    annual_compounding = principal
    for _ in range(years):
        annual_compounding = annual_compounding * (1+ rate / 100) + contribution
    
    return round(annual_compounding,2)

print(compound_interest(principal, rate, contribution, years))

