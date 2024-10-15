def sad_spectators(matrix_heights):
    unsatisfied_spectators = []

    rows = len(matrix_heights)
    columns = len(matrix_heights[0])

    for j in range(0, columns):
        for i in range(0, rows-1):
            if matrix_heights[i][j] > matrix_heights[i+1][j]:
                unsatisfied_spectators.append((i + 1, j))

    return unsatisfied_spectators


print(sad_spectators([[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]]))

