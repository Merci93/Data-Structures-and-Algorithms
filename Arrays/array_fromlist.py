from array import array


def array_fromlist(arg_1: array, arg_2: list) -> array:
    """Add a list into an array"""
    arg_1.fromlist(arg_2)
    return arg_1


input_1 = array("i", [1, 2, 3, 4, 5, 6])
input_2 = [19, 20, 21, 22, 23]

result = array_fromlist(input_1, input_2)
print(result)
