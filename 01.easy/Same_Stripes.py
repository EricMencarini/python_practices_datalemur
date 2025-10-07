#https://datalemur.com/questions/python-same-stripes

'''
You are given an m x n matrix. Your task is to determine if the matrix 
has diagonal stripes where all elements in each diagonal from top-left to 
bottom-right are of the same stripe—that is, they are identical.

In this context, each diagonal stripe runs from the top-left corner to the 
bottom-right corner of the matrix. Check if every diagonal stripe consists 
entirely of the same number.

Return True if all diagonal stripes are of the same stripe, otherwise return False.

'''
def is_same_stripes(matrix) -> bool:
    diagonals = {}
    
    for x in range(len(matrix)):
      for y in range(len(matrix[0])):
        
        if x - y in diagonals and diagonals[x - y] != matrix[x][y]:
          return False
        else:
          diagonals[x - y] = matrix[x][y]
    return True      