def best_scores(arr: list) -> list:
    """function to get the top two scores in a list."""
    max_val_1, max_val_2 = float("-inf"), float("-inf")

    for num in arr:
        if num > max_val_1:
            max_val_2 = max_val_1
            max_val_1 = num
        elif num > max_val_2 and num != max_val_1:
            max_val_2 = num
    return max_val_1, max_val_2


arr = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
output = best_scores(arr)
print(output)
