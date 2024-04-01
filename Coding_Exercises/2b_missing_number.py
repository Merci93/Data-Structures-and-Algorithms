"""Using n-series"""


def missing_number(arr: list, n: int) -> int:
    n_series_sum = n * (n + 1) / 2
    arr_sum = sum(arr)

    return n_series_sum - arr_sum


val = [1, 2, 3, 4, 5, 6, 8, 9, 10]
missing_n = missing_number(val, 10)
print(missing_n)
