def middle(arr: list) -> list:
    """Function to return the middle values in an array."""
    return arr[1:-1]


arr = [1, 7, 3, 4, 9, 5]
output = middle(arr)
print(output)
