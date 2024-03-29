from array import array


def count_element(arg_1: array, arg_2: int) -> int:
    """Return the number of occurrence of an element in an array."""
    return arg_1.count(arg_2)


input_1 = array("i", [19, 20, 21, 22, 23, 13, 10, 20])
input_2 = 20

result = count_element(input_1, input_2)
print(result)
