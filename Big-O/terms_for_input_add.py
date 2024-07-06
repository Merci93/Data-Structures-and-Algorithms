"""
Add time complexities
runtime: O(a + b)
"""

def print_items(a: int, b: int) -> None:
    """
    Print items

    :param a: first integer
    :param b: second integer
    """
    for i in range(a):
        print(i)
    
    for j in range(b):
        print(j)
    
print_items(2, 4)
