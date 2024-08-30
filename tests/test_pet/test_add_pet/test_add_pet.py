import json
import os
from utils.logger import get_logger

logger = get_logger()

def test_add_pet(pet_api):
    logger.info("Starting test: Adding a new pet")

    pet_file = os.path.join(os.path.dirname(__file__), '../../../data/new_pet.json')
    with open(pet_file, 'r') as file:
        new_pet = json.load(file)
    logger.info(f"Loaded pet data from {pet_file}: {new_pet}")

    response = pet_api.add_pet(new_pet)
    logger.info(f"Received response with status code: {response.status_code}")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    logger.info("Status code is 200 as expected")

    pet_name = response.json().get("name")
    assert pet_name == "Rex", f"Expected pet name to be 'Rex', got {pet_name}"
    logger.info(f"Pet name is '{pet_name}' as expected")