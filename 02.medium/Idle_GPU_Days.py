#https://datalemur.com/questions/python-idle-gpu-days

'''
At your big-tech company, teams are fighting tooth and nail to train their AI models 
on the company’s shiny new NVIDIA GPUs. 
It’s like the Hunger Games but with less archery and more coding.

The GPUs are in such high demand that some teams “accidentally” (totally on purpose) 
overlap their training sessions. It’s chaos. The GPU cluster is booked for days on end,
 and now everyone’s looking for gaps to squeeze in their own usage.

Unlike those greedy GPU hogs, your team has been given strict instructions: 
you can only run your training on days when nobody else is using the GPUs. 
Your VP made it crystal clear that overlapping sessions are not an option.

You’re given two things:

An integer days, representing the total number of days the GPUs are 
available (from day 1). A 2D array training_sessions where 
training_sessions[i] = [start_i, end_i] shows when team i is hogging the GPUs.
Your mission is to figure out how many days the GPUs are sitting idle so that your 
team can swoop in and get some guilt-free training time.

'''


training_sessions = [[2, 4], [1, 5], [7, 8]] 
days = 9

def gpu_idle_days(days, training_sessions):
	ts_fill = [list(range(start, end+1)) for start, end in training_sessions]
	flat = [x for z in ts_fill for x in z]
	ordered_flat = sorted(set(flat))
	return days - len(ordered_flat)

print(gpu_idle_days(days, training_sessions))
