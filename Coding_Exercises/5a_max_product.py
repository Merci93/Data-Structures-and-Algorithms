def max_product(arr: list) -> None:
    """max product of two integers"""
    max_prod = float("-inf")
    value_1, value_2 = 0, 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr_prod = arr[i] * arr[j]
            if arr_prod > max_prod:
                value_1, value_2, max_prod = arr[i], arr[j], arr_prod

    return f"{value_1} * {value_2} = {max_prod}"


arr = [1, 7, 3, 4, 9, 5]
output = max_product(arr)
print(output)
