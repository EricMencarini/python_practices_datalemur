#https://datalemur.com/questions/python-clock-wise-matrix-rotation

'''
You are given an n x n 2D matrix representing an image, and you need to rotate the 
image by 90 degrees clockwise. You are basically being asked to implement the 
functionality of numpy.rot90(matrix, k=-1) (without actually using any helper 
functions or outside libraries).

'''
matrix = [[5, 1], [6, 2]]

'''
rotate 90 degress and see if matches
'''
def rotate_90_clockwise(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

rotate_90_clockwise(matrix)
#print(matrix)