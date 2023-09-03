def add_numbers(x: int) -> int:
    """
    A constant time complexity, O(1), to add a number to itself.
    Performs only one operation, no matter how the input increases, thus the most efficient.

    :param x: input variable
    :return: sum of input variable
    """
    return x + x

print(add_numbers(5))