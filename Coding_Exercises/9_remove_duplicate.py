def remove_duplicate(arr: list) -> list:
    """Remove duplicates from an array or list."""
    unique_values = []
    seen = set()

    for num in arr:
        if num not in seen:
            unique_values.append(num)
            seen.add(num)
    return unique_values


arr = [1, 1, 2, 3, 5, 6, 5, 6, 7, 8, 9, 0, 6, 0]
output = remove_duplicate(arr)
print(output)
