def linear_search(arg_list: list, target: int | str) -> int:
    """Return the index of a value in a list."""
    for idx, value in enumerate(arg_list):
        if target == value:
            return idx
    return -1


input_1 = [19, 20, 21, 22, 23, 24, 25, 26, 27]

result = linear_search(input_1, 23)
print(result)

result_2 = linear_search(input_1, 50)
print(result_2)
