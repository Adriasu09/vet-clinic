"""Essential tests for the Pet endpoints."""


def create_owner(client):
    response = client.post("/owners/", json={
        "first_name": "Ana", "last_name": "García",
        "email": "ana@example.com", "phone": "600111222",
    })
    return response.json()["id"]


def test_create_pet(client):
    owner_id = create_owner(client)
    response = client.post("/pets/", json={
        "name": "Firulais", "species": "dog", "breed": "labrador",
        "birth_date": "2020-05-01", "owner_id": owner_id,
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Firulais"


def test_create_pet_owner_not_found(client):
    response = client.post("/pets/", json={
        "name": "Firulais", "species": "dog", "breed": "labrador",
        "birth_date": "2020-05-01", "owner_id": 9999,
    })
    assert response.status_code == 404