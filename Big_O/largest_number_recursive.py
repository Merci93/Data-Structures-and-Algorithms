"""
Find the largest number in a given array using recursion.
"""

def find_largest_number(sample_array: list, n: int) -> None:
    """
    Iterate through a list and return the largest number.

    :param sample_array: A list of integers/floats
    :param n: length of array
    """
    if n == 1:
        return sample[0]
    return max(sample_array[n-1], find_largest_number(sample_array, n-1))

sample = [1, 3, 7, 20, 11, 19, 0, 33, 22, 5, 13, 99]
print(find_largest_number(sample, len(sample)))
