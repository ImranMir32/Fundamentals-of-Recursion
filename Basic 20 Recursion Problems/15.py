def multiply_matrices(mat1, mat2):
    def multiply_helper(row, col):
        if row == len(mat1):
            return []
        if col == len(mat2[0]):
            return [multiply_helper(row + 1, 0)]
        element = 0
        for k in range(len(mat1[0])):
            element += mat1[row][k] * mat2[k][col]
        return [element] + multiply_helper(row, col + 1)

    result = multiply_helper(0, 0)

    return [result[i:i+len(mat2[0])] for i in range(0, len(result), len(mat2[0]))]

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"element - [{i}],[{j}] : ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

rows1 = int(input("Input number of rows for the first matrix: "))
cols1 = int(input("Input number of columns for the first matrix: "))

rows2 = int(input("Input number of rows for the second matrix: "))
cols2 = int(input("Input number of columns for the second matrix: "))

print("Input elements in the first matrix:")
matrix1 = input_matrix(rows1, cols1)

print("Input elements in the second matrix:")
matrix2 = input_matrix(rows2, cols2)

print("\nHere are the elements of First matrix:")
print_matrix(matrix1)

print("\nHere are the elements of Second matrix:")
print_matrix(matrix2)

result_matrix = multiply_matrices(matrix1, matrix2)

print("\nThe multiplication of two matrices is:")
print_matrix(result_matrix)
