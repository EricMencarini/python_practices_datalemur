#https://datalemur.com/questions/python-spiral-matrix
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

def spiral_order(matrix):
    #print(matrix)
    spiral = []

    while matrix:
        e1 = matrix.pop(0)
        spiral += e1
        #print(spiral,e1)
        e2 = [row.pop(-1) for row in matrix if row]
        spiral += e2
        #print(spiral,e2)
        if matrix:
            e3 = matrix.pop(-1)[::-1]
            spiral += e3
            #print(spiral,e3)
        e4 = [row.pop(0) for row in reversed(matrix) if row]
        spiral += e4
        #print(spiral,e4)

    return spiral

#print(spiral_order(matrix))