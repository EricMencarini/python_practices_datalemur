#https://datalemur.com/questions/python-intersection-of-two-lists

import numpy as np

a = [1,2,3]
b = [3,4,5]
c = [10,20,30]
d = [20,30,40]

def intersection(a,b):
    intersection = [x for x in a if x in b]
    return intersection

def intersection_numpy(c,d):
    intersection = np.intersect1d(c,d)
    return intersection.tolist() 

print(intersection(a,b))
print(intersection(c,d))
