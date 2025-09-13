#https://datalemur.com/questions/python-is-anagram

s = "lemur" 
t = "lemer"

#Solution 1
def is_anagram_one(s,t) -> bool:
    return sorted(s) == sorted(t)
    
is_anagram_one(s,t)

#Solution 2
def is_anagram(s, t):
    chars_s = sorted(s)
    chars_t = sorted(t)
    
    s = 0
    t = 0

    if len(chars_s) != len(chars_t):
        return False
    
    while len(chars_s) > s and len(chars_t) > t:
        if chars_s[s] == chars_t[t]:
            s += 1
            t += 1 

        else:
            return False
            break
    return True
