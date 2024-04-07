def best_scores(arr: list) -> list:
    """function to get the top two scores in a list."""
    unique_vals = list(set(arr))
    unique_vals.sort(reverse=True)
    max_val_1, max_val_2 = unique_vals[0], unique_vals[1]
    return max_val_1, max_val_2


arr = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
output = best_scores(arr)
print(output)
