# https://datalemur.com/questions/python-roman-to-integer


'''
Transform roman numbers
'''
def romanToInt(s):
  r_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5,'I': 1}
  i  = 0
  c = s[0]
  
  for r in s:
    if r_num[c] < r_num[r]:
      i = i - (2 * r_num[c])
    i = i + r_num[r]
    c = r
  
  return(i)

romanToInt("XIX")