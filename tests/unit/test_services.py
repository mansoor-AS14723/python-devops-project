from app.services import get_all_items, get_item_by_id


def test_get_all_items_returns_all_items():
    items = get_all_items()

    assert len(items) == 3
    assert items[0]["name"] == "Laptop"


def test_get_item_by_id_returns_existing_item():
    item = get_item_by_id(1)

    assert item is not None
    assert item["id"] == 1
    assert item["name"] == "Laptop"


def test_get_item_by_id_returns_none_for_missing_item():
    item = get_item_by_id(99)

    assert item is None