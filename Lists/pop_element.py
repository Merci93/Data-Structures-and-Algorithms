def pop_element(arg_1: list, idx: int = -1) -> list:
    """Remove the last element in an array"""
    arg_1.pop(idx)
    return arg_1


input_1 = [1, 2, 3, 4, 5, 6]

result = pop_element(input_1)
print(result)
