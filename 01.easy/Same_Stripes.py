#https://datalemur.com/questions/python-same-stripes

def is_same_stripes(matrix) -> bool:
    diagonals = {}
    
    for x in range(len(matrix)):
      for y in range(len(matrix[0])):
        
        if x - y in diagonals and diagonals[x - y] != matrix[x][y]:
          return False
        else:
          diagonals[x - y] = matrix[x][y]
    return True      