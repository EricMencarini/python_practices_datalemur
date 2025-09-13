#https://datalemur.com/questions/python-counting-letters-in-numbers

N = 52

def total_letters(N):
    one_to_nineteen = {
        0:"zero", 1:"one",2:"two",3:"three",4:"four",5:"five",
        6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
        11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",
        15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"
    }
    tens = {
        20:"twenty",30:"thirty",40:"forty",50:"fifty",
        60:"sixty",70:"seventy",80:"eighty",90:"ninety"
    }

    def number_to_words(num):
        if num == 1000: #limited by the question
            return "one thousand"
        
        elif num >= 100:
            hundred_part = one_to_nineteen[num // 100] + " hundred"
            remainder = num % 100
            if remainder == 0:
                return hundred_part
            else:
                return hundred_part + " and " + number_to_words(remainder)
        elif num >= 20:
            ten_part = tens[(num // 10) * 10]
            remainder = num % 10
            if remainder == 0:
                return ten_part
            else:
                return ten_part + "-" + one_to_nineteen[remainder]
        else:
            return one_to_nineteen[num]

    n_to_text = 0
    
    while N > 0:
        word = number_to_words(N)
        cleaned = word.replace(" ", "").replace("-", "")
        n_to_text += len(cleaned)
        N -= 1

    return n_to_text


print(total_letters(N))