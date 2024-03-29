from array import array


def array_to_list(arg_1: array) -> list:
    """COnvert an array to list."""
    return arg_1.tolist()


input_1 = array("i", [19, 20, 21, 22, 23])

result = array_to_list(input_1)
print(result)
