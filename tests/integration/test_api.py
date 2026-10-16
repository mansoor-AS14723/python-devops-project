from app.main import app


def test_home_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Python DevOps Demo API"
    assert response.json["status"] == "running"


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_list_items_endpoint():
    client = app.test_client()

    response = client.get("/items")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_existing_item_endpoint():
    client = app.test_client()

    response = client.get("/items/1")

    assert response.status_code == 200
    assert response.json == {"id": 1, "name": "Laptop"}


def test_get_missing_item_endpoint():
    client = app.test_client()

    response = client.get("/items/99")

    assert response.status_code == 404
    assert response.json == {"error": "Item not found"}