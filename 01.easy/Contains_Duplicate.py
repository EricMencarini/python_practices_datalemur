#https://datalemur.com/questions/python-contains-duplicate

input = [1,3,5,7,1]
input2 = [1,3,5,7,1]

'''
verify duplicate
'''
def contains_duplicate(input)-> bool:
  return len(input) > len(set(input))
  
print(contains_duplicate(input))  