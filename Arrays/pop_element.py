from array import array


def pop_element(arg_1: array) -> array:
    """Remove the last element in an array"""
    arg_1.pop()
    return arg_1


input_1 = array("i", [1, 2, 3, 4, 5, 6])

result = pop_element(input_1)
print(result)
