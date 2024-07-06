import numpy as np


def find_number(arr: list, number) -> int | bool:

    for i in range(len(arr)):
        if arr[i] == number:
            return i
    return False


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output_1 = find_number(arr, 7)
print(output_1)

output_2 = find_number(arr, 71)
print(output_2)
