"""
A recursive program calling itself and assigning stack memory, and takes a lot of space
since the processes increase recursively. This can be viewed in debug mode.   
"""

def check_recursive(n: int) -> int:
    """
    Checks if an integer value is less or equal to 0.

    :param n: integer value
    :return: integer value less than or equal to zero
    """
    if n <= 0:
        return 0
    return n + check_recursive(n-1)

check_recursive(5)
