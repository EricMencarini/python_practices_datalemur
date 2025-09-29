#https://datalemur.com/questions/python-idle-gpu-days

training_sessions = [[2, 4], [1, 5], [7, 8]] 
days = 9

def gpu_idle_days(days, training_sessions):
	ts_fill = [list(range(start, end+1)) for start, end in training_sessions]
	flat = [x for z in ts_fill for x in z]
	ordered_flat = sorted(set(flat))
	return days - len(ordered_flat)

print(gpu_idle_days(days, training_sessions))
