import json
import os

def test_add_pet(pet_api):
    pet_file = os.path.join(os.path.dirname(__file__), '../data/new_pet.json')
    with open(pet_file, 'r') as file:
        new_pet = json.load(file)

    response = pet_api.add_pet(new_pet)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"
