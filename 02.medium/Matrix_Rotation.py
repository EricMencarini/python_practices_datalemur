#https://datalemur.com/questions/python-martix-rotation

#first input
mat = [[1,0,1],[0,0,1],[1,0,1]]
target = [[1,0,1],[1,0,0],[1,0,1]]

#second input
mat2 = [[0, 1],[1, 0]] 
target2 = [[1, 1],[0, 0]]

'''
find if it's possible to make mat equal to target by rotating mat in 90-degree increments
'''
def find_rotation(mat, target):
    for _ in range(4):  # tenta 0°, 90°, 180°, 270°
        if mat == target:
            return True
        mat = [list(row) for row in zip(*mat[::-1])]  # rotaciona 90°
        #print(mat)
    return False

#print(find_rotation(mat, target))
#print(find_rotation(mat2, target2))