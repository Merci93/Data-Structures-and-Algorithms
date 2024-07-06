"""
Find the two maximum numbers by sorting the array in a reverse order and
select the first two values which by default are the maximum numbers.
"""


def max_product(arr: list) -> str:
    """Max product in an array."""
    arr.sort(reverse=True)
    return f"{arr[0]} * {arr[1]} = {arr[0] * arr[1]}"


arr = [1, 7, 3, 4, 9, 5]
output = max_product(arr)
print(output)
