def delete_element(arg_1: list, start: int, end: int = None) -> list:
    """Slice a list."""
    del arg_1[start:end]
    return arg_1


input_1 = [19, 20, 21, 22, 23, 24, 25, 26, 27]

result_1 = delete_element(input_1, 0, 1)
print(result_1)

result_2 = delete_element(input_1, 3, 4)
print(result_2)
