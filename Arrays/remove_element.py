"""
Compared to pop, this is not efficient as it removes an element and
the array memory is readjusted to account for the free memory.
"""

from array import array


def remove_element(arg_1: array, arg_2: int) -> array:
    """Remove the first occurrence of an element in an array."""
    arg_1.remove(arg_2)
    return arg_1


input_1 = array("i", [1, 1, 2, 3, 4, 5, 6])
input_2 = 1

result = remove_element(input_1, input_2)
print(result)
