# https://datalemur.com/questions/python-roman-to-integer

'''
Given a valid Roman numeral, convert it to an integer.

in case you don't think about the Roman empire that often, 
and need a crash-course on how to go from Superbowl "XLIV" to an actual number, 
here's the table mapping the numerals to their values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
The numerals are generally written from largest to smallest from left to right. 
For example, the number 11 is written as XI, where X represents 10 and I represents 
1, so the total is 11.

Similarly, XXX would be 30 (unless we're talking about your browser's search history).
'''

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