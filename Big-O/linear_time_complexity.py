
def print_items(n: int) -> None:
    """
    A linear time complexity, O(n), to print items in a sorted list.
    The execution changes as the operation proceeds, thus less efficient than the constant but has
    a linear dependence on the variable.

    :param n: Input variable
    """
    for i in range(n):
        print(i)
    
print_items(10)
