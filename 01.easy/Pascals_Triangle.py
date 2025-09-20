#https://datalemur.com/questions/python-pascals-triangle

numRows = 3

def generate(numRows):
  result = list()
  if numRows >= 1:
    for i in range(0, numRows):
      row = [1] * (i + 1)
      for j in range(1, i):
        row[j] = result[i-1][j-1] + result[i-1][j]
      result.append(row)
  
  return result

generate(3)