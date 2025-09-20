#https://datalemur.com/questions/python-palindrome

def isPalindrome(phrase: str) -> bool:
    clean = ''.join(c.lower() for c in phrase if c.isalnum())
    return clean == clean[::-1]