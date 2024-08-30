import json
import os

def test_add_pet(pet_api):
    pet_file = os.path.join(os.path.dirname(__file__), '../data/new_pet.json')
    with open(pet_file, 'r') as file:
        new_pet = json.load(file)

    response = pet_api.add_pet(new_pet)

    print(f"Response status code: {response.status_code}")
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"

def test_add_pet_missing_field(pet_api):
    pet_file = os.path.join(os.path.dirname(__file__), '../data/new_pet_missing_field.json')
    with open(pet_file, 'r') as file:
        pet_missing_field = json.load(file)
    response = pet_api.add_pet(pet_missing_field)

    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.json()}")

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json()["status"] == "xoxo", "Expected status to be 'xoxo"

def test_add_duplicate_pet(pet_api):
    pet_file = os.path.join(os.path.dirname(__file__), '../data/new_pet.json')
    with open(pet_file, 'r') as file:
        new_pet = json.load(file)

    response = pet_api.add_pet(new_pet)
    assert response.status_code == 200, f"Expected 200 OK, but got {response.status_code}"

    duplicate_pet = pet_api.add_pet(new_pet)
    assert duplicate_pet.status_code == 200, f"Expected 200 OK, but got {response.status_code}"

    fetched_pet = pet_api.get_pet(new_pet["id"]).json()
    assert fetched_pet["name"] == new_pet["name"], f"Expected name to be {new_pet['name']}, but got {fetched_pet['name']}"
