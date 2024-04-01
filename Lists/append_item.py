"""Insert a value at the end of a list."""


def append_value(list_item: list, value: int | str) -> list:
    list_item.append(value)
    return list_item


items = [0, 2, 4, 1, 7]
print(items)

updated_items = append_value(items, 50)
print(updated_items)
