from array import array


def get_index(arg_1: array) -> array:
    """reverse a given array."""
    arg_1.reverse()
    return arg_1


input_1 = array("i", [19, 20, 21, 22, 23])

result = get_index(input_1)
print(result)
