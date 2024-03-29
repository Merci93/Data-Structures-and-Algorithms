"""
This is not efficient compared to append as it rearranges the whole array,
except it's been added after the last element in the array.
"""

from array import array


def insert_value(arg_1: array, arg_2: int, position: int) -> array:
    """Insert a given integer into an array of integers, in a given position."""
    arg_1.insert(position, arg_2)
    return arg_1


input_1 = array("i", [10, 20, 30, 40, 50])
input_2 = 99
position = 1

result = insert_value(input_1, input_2, position)
print(result)
