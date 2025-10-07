#https://datalemur.com/questions/python-add-another-one

''''
We're trying to create a digital clone of DJ Khaled. No fancy AI or alorithms needed.
Just take a number and add another one:

More specifically, you are given an integer array digits, 
where each digits[i] is the ith digit of positive whole number. 

It is ordered from most significant to least significant digit.

Return an array of digits of the number after adding another one to the input.
'''

digits = [1,2,3]

def another_one(digits):
    fullnumber = int(''.join(map(str,digits)))
    fullnumber += 1
    fullnumber_split = list(map(int,str(fullnumber)))
    return fullnumber_split

another_one(digits)