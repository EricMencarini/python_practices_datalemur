#https://datalemur.com/questions/python-pearson-correlation-coefficient

import numpy as np

def corr(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.corrcoef(x, y)[0, 1]

