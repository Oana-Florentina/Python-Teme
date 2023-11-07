# Write a Python class that simulates a matrix of size NxM,
# with N and M provided at initialization. The class should provide
# methods to access elements (get and set methods) and some
# mathematical functions such as transpose, matrix multiplication
# and a method that allows iterating through all elements form
# a matrix an apply a transformation over them (via a lambda function).

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = sum(self.get(i, k) * other.get(k, j) for k in range(self.cols))
                result.set(i, j, dot_product)
        return result

    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, func(self.get(i, j)))

    def __str__(self):
        matrix_str = ""
        for i in range(self.rows):
            row_str = " ".join(map(str, self.data[i]))
            matrix_str += row_str + "\n"
        return matrix_str


matrix = Matrix(3, 2)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(1, 0, 3)
matrix.set(1, 1, 4)
matrix.set(2, 0, 5)
matrix.set(2, 1, 6)

print("Original Matrix:")
print(matrix)

transformed_matrix = matrix.transpose()
print("Transposed Matrix:")
print(transformed_matrix)

matrix2 = Matrix(2, 2)  # Change the dimensions to match the matrix multiplication requirement.
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(1, 0, 9)
matrix2.set(1, 1, 10)


product = matrix.multiply(matrix2)
print("Matrix Multiplication Result:")
print(product)

matrix.apply(lambda x: x * 2)
print("Matrix after applying a transformation (doubling each element):")
print(matrix)
