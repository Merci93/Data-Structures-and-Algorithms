def pair_sum(arr: list, value: int) -> list:
    """Pair sum of values in an array"""
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == value:
                pairs.append(f"{arr[i]} + {arr[j]}")
    return pairs


arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
output = pair_sum(arr, 7)
print(output)
