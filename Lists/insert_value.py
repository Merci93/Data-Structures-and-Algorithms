"""Insert a value in a list at a specified index."""


def insert_value(list_item: list, idx: int, value: int | str) -> list:
    list_item.insert(idx, value)
    return list_item


items = [0, 2, 4, 1, 7]
print(items)

updated_items = insert_value(items, 0, 50)
print(items)
