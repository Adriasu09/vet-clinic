"""Essential tests for the Owner endpoints."""


def owner_payload(**overrides):
    data = {
        "first_name": "Ana",
        "last_name": "García",
        "email": "ana@example.com",
        "phone": "600111222",
    }
    data.update(overrides)
    return data


def test_create_owner(client):
    response = client.post("/owners/", json=owner_payload())
    assert response.status_code == 201
    assert response.json()["email"] == "ana@example.com"


def test_get_owner_not_found(client):
    response = client.get("/owners/9999")
    assert response.status_code == 404


def test_create_owner_duplicate_email(client):
    client.post("/owners/", json=owner_payload())
    response = client.post("/owners/", json=owner_payload(phone="600999999"))
    assert response.status_code == 409