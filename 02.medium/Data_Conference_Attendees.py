#https://datalemur.com/questions/python-data-conference-attendees

answers = [2, 1, 1]

def min_attendees(answers):
    total_answer = 0
    d_answer = {}  

    for ans in answers:
        if ans not in d_answer:
            total_answer += ans + 1
            d_answer[ans] = 1
        else:
            if d_answer[ans] < ans + 1:
                d_answer[ans] += 1
            else:
                total_answer += ans + 1
                d_answer[ans] = 1
    return total_answer

print(min_attendees(answers))