matrix = [[1,2],[3,4]]
r = 1
c = 4
output = [1,2,3,4]

def reshape_matrix(matrix, r, c):
    '''
    INPUT: Two dimensional list, and number of rows and columns of reshaped matrix
    OUTPUT: Reshaped matrix
    '''
    pass
    row_num = len(matrix)
    column_num = len(matrix[0])

    if row_num * column_num != r * c:
        return matrix

    reshape = []
    row = []

    for i in range(row_num):
        for j in range(column_num):
            row.append(matrix[i][j])
            if len(row) == c:
                reshape.append(row)
                row = []
    return reshape

print(reshape_matrix(matrix, r, c))




    