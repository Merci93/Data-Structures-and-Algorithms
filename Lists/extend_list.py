"""Insert a list to another list."""


def extend_list(list_1: list, list_2: list) -> list:
    list_1.extend(list_2)
    return list_1


item_1 = [0, 2, 4, 1, 7]
item_2 = [10, 20, 30, 40, 50, 60]

updated_items = extend_list(item_1, item_2)
print(updated_items)
