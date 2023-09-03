"""
A recursive program calling itself and assigning stack memory, and clears the memory before
reassigning. Uses O(1) complexity. This can be viewed in debug mode.   
"""

def check_recursive(n: int) -> int:
    """
    Adds integer values

    :param n: integer value
    :return: integer value less than or equal to zero
    """
    total  = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
        print(total)
    return total

def pair_sum(a: int, b: int) -> int:
    """
    Add two integers

    :param a: first integer
    :param b: second integer
    :return: sum of first and second integer
    """
    return a + b

check_recursive(5)