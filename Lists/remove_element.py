def remove_element(arg_1: list, element: int | str) -> list:
    """Slice a list."""
    arg_1.remove(element)
    return arg_1


input_1 = [19, 20, 21, 22, 23, 24, 25, 26, 27]

result = remove_element(input_1, 23)
print(result)
