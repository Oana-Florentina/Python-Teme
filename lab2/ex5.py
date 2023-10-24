#5. Write a function that receives as parameter a matrix and will return
# the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def matrixReplace(A,n):
    for i in range (0,n):
        for j in range (0,i):
            A[i][j]=0
    return A
matrix = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]

    ]
result_matrix = matrixReplace(matrix, 4)

# Print the matrix row by row
for row in result_matrix:
    print(row)