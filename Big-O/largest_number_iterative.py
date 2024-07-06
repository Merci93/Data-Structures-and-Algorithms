"""
Find the largest number in a given array
"""

def find_largest_number(sample_array: list) -> None:
    """
    Iterate through a list and return the largest number.

    :param sample_array: A list of integers/floats
    """
    largest_number = sample_array[0]
    for idx in range(1, len(sample_array)):
        if sample_array[idx] > largest_number:
            largest_number = sample_array[idx]
    print(largest_number)

sample = [1, 3, 7, 20, 11, 19, 0, 33, 22, 5, 13, 99]
find_largest_number(sample)
