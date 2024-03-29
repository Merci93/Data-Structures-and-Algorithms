from array import array


def append_value(array_value: array, value: int) -> array:
    """Append value to an array."""
    array_value.append(value)
    return array_value


input_array = array("i", [1, 2, 3, 4, 5])
value = 6

result = append_value(input_array, value)
print(result)
