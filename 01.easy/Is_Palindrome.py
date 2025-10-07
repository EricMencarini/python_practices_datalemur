#https://datalemur.com/questions/python-palindrome

'''
Given a string phrase, return True if it is a palindrome, otherwise return False.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Challenge: Try solving this without using extra memory. 
Specifically, solve it without making a copy of phrase.

Clarifications:

phrase is made up of only: letters, numbers, spaces, and standard punctuation/symbols
'''


def isPalindrome(phrase: str) -> bool:
    clean = ''.join(c.lower() for c in phrase if c.isalnum())
    return clean == clean[::-1]