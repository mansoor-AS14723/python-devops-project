ITEMS = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Keyboard"},
    {"id": 3, "name": "Mouse"},
]


def get_all_items():
    return ITEMS


def get_item_by_id(item_id):
    for item in ITEMS:
        if item["id"] == item_id:
            return item

    return None