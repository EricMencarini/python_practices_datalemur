#https://datalemur.com/questions/python-add-another-one

digits = [1,2,3]

def another_one(digits):
    fullnumber = int(''.join(map(str,digits)))
    fullnumber += 1
    fullnumber_split = list(map(int,str(fullnumber)))
    return fullnumber_split

another_one(digits)