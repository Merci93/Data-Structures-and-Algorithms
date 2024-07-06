def print_items(n: int) -> None:
    """
    A quadratic time complexity, O(n^2) or O(n^n). This is very inefficient since there is a
    quadratic increase as n increases, leading to multiple operations.

    :param n: Input variable
    """
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(f"{i}{j}{k}")

print_items(10)
