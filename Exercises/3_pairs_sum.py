def pairs_sum(arr: list, target: int) -> list[int]:
    """pair integer sums"""

    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] != arr[j]) and (arr[i] + arr[j] == target):
                pairs.append([i, j])
    return pairs


arr = [1, 2, 3, 2, 4, 5, 6, 3]
output = pairs_sum(arr, 6)
print(output)
