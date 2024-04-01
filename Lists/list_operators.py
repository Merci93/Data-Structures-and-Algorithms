def concat_lists(list_a: list, list_b: list) -> list:
    """COncatenate two lists."""
    return list_a + list_b


def multiply_value(list_a: list, value: int) -> list:
    """Multiply a list given an integer."""
    return list_a * value


input_1 = [19, 20, 21, 22]
input_2 = [23, 24, 25, 26, 27]

concat = concat_lists(input_1, input_2)
print(concat)

mult = multiply_value(input_1, 2)
print(mult)
