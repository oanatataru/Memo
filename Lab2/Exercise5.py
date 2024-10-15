def process(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i > j:
                matrix[i][j] = 0

    return matrix


matrix = [
    [1, 21, 1],
    [4, 1, 1],
    [1, 1, 1]
]

new_matrix = process(matrix)

for row in new_matrix:
    print(row)
