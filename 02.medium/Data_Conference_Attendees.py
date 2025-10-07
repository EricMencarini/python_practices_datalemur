#https://datalemur.com/questions/python-data-conference-attendees

'''
You’re at a Data Science conference with an unknown number of attendees. 
The attendees have a wide range of titles, such as Data Scientist, Data Analyst, 
ML Product Manager, ML Engineer, Founder, CTO, and others.

During the event, you ask a sample of n attendees the following question:

"How many other people here have you met with the same title as you?"

Each response is recorded in the answers array, where answers[i] is the 
response of the i-th person you surveyed. Assume that each person you surveyed has 
encountered every other person at the conference with the same title.

Given the array answers, return the minimum possible total number of attendees at 
the conference.

'''
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