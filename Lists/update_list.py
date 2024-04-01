"""A function to update a list with a given value."""


def update_list(list_item: list, idx: int, value: int | str) -> list:
    list_item[idx] = value
    return list_item


items = [0, 2, 4, 1, 7]
print(items)

updated_items = update_list(items, 3, 100)
print(updated_items)
