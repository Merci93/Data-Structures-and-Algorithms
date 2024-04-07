def diagonal_sum(arr: list) -> None:
    """Function to calculate the diagonal sum of a 2-d array"""
    dim = len(arr)

    if dim <= 1:
        return -1

    diag_sum = 0
    for i in range(dim):
        diag_sum += arr[i][i]
    return diag_sum


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
output = diagonal_sum(arr)
print(output)
