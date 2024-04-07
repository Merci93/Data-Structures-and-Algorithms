def max_product(arr: list) -> str:
    """Max product integers in an array"""
    val_1, val_2 = 0, 0

    for num in arr:
        if num > val_1:
            val_2 = val_1
            val_1 = num
        elif num > val_2:
            val_2 = num
    return f"{val_1} * {val_2} = {val_1 * val_2}"


arr = [1, 7, 3, 4, 9, 5]
output = max_product(arr)
print(output)
