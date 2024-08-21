import pytest

def test_add_pet(pet_api):
    new_pet = {
        "id": 99999,
        "name": "Rex",
        "photoUrls": ["https://images.app.goo.gl/vZDewg4s8hBy1SPv5"],
        "tags": [{"id": 2, "name": "sharp"}],
        "status": "not available"
    }
    response = pet_api.add_pet(new_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"
