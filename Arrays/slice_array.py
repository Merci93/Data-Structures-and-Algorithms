from array import array


def get_index(arg_1: array, start: int, end: int = None) -> array:
    """Slice an array."""
    return arg_1[start:end]


input_1 = array("i", [19, 20, 21, 22, 23, 24, 25, 26, 27])
start = 2
end = 5

result_1 = get_index(input_1, start, end)
result_2 = get_index(input_1, start)
print(result_1)
print(result_2)
