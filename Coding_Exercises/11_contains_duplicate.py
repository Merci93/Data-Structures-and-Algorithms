def contains_duplicate(arr: list) -> bool:
    """Check for duplicates"""
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


arr = [1, 2, 3, 4, 5, 5, 6, 7]
output = contains_duplicate(arr)
print(output)
