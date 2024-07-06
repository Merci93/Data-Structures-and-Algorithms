"""
Logarithmic time complexity
"""

def print_items(n: int) -> None:
    """
    Examine logarithmic time complexity given an integer value n.

    :param n: integer value
    """
    sum = 0
    i = 1
    while i <= n:
        sum += i
        print(f"sum = {sum}")
        i *= 2
        print(f"i = {i}")
    
print_items(5)
