"""
Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and
row to 0 and then return the matrix.

  Examples 1:
Input:
 matrix=[
 [1,1,1],
 [1,0,1],
 [1,1,1]]

Output:
 [[1,0,1],
 [0,0,0],
 [1,0,1]]

Explanation:
 Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

Input:
 matrix=[
 [0,1,2,0],
 [3,4,5,2],
 [1,3,1,5]
 ]

Output:
[
[0,0,0,0],
[0,4,5,0],
[0,3,1,0]]

Explanation:
Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0


"""


def zero_matrix(input_matrix):
    m = len(input_matrix)
    n = len(input_matrix[0])
    zero_row = set()
    zero_col = set()
    for i in range(m):
        for j in range(n):
            if input_matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for i in zero_row:
        t = 0
        while t < n:
            input_matrix[i][t] = 0
            t += 1
    for j in zero_col:
        t = 0
        while t < m:
            input_matrix[t][j] = 0
            t += 1
    return input_matrix


if __name__ == "__main__":
    inp = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(zero_matrix(inp))

    inp = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(zero_matrix(inp))
