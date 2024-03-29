from array import array


def get_index(arg_1: array, arg_2: int) -> int:
    """Return the index of a given value in an array."""
    return arg_1.index(arg_2)


input_1 = array("i", [19, 20, 21, 22, 23])
input_2 = 21

result = get_index(input_1, input_2)
print(result)
