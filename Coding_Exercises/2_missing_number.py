
def missing_number(arr, n):
    if len(arr) == n:
        return None

    missing_values = []

    for i in range(1, n + 1):
        if i not in arr:
            missing_values.append(i)

    return missing_values[0]


val = [1, 2, 3, 4, 5, 6, 8, 9, 10]
missing_n = missing_number(val, 10)
print(missing_n)
