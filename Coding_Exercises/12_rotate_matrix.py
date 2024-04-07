def rotate(matrix: list[list]) -> list[list]:
    """Rotate a given matrix 90 degrees clockwise."""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = rotate(matrix)
print(output)
