def slice_element(arg_1: list, start: int, end: int = None) -> list:
    """Slice a list."""
    return arg_1[start:end]


input_1 = [19, 20, 21, 22, 23, 24, 25, 26, 27]
start = 2
end = 5

result_1 = slice_element(input_1, start, end)
print(result_1)

result_2 = slice_element(input_1, start)
print(result_2)
