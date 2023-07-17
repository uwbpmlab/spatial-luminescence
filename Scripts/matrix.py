def rearrange_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            element = matrix[i][j]
            new_i = (i % 3) * 3 + j // 3
            new_j = (i // 3) * 3 + j % 3
            new_matrix[new_i][new_j] = element

    return new_matrix


# Example usage
matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [10, 11, 12, 13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24, 25, 26, 27],
          [28, 29, 30, 31, 32, 33, 34, 35, 36],
          [37, 38, 39, 40, 41, 42, 43, 44, 45],
          [46, 47, 48, 49, 50, 51, 52, 53, 54],
          [55, 56, 57, 58, 59, 60, 61, 62, 63],
          [64, 65, 66, 67, 68, 69, 70, 71, 72],
          [73, 74, 75, 76, 77, 78, 79, 80, 81]]

new_matrix = rearrange_matrix(matrix)
for row in new_matrix:
    print(row)