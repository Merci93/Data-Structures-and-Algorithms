from array import array


def extend_array(arg_1: array, arg_2: array) -> array:
    """Extend a given array."""
    arg_1.extend(arg_2)
    return arg_1


input_1 = array("i", [1, 2, 3, 4, 5, 6])
input_2 = array("i", [10, 12, 12])

result = extend_array(input_1, input_2)
print(result)
