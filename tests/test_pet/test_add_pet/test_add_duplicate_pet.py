import json, os
from utils.logger import get_logger

logger = get_logger()

def test_add_duplicate_pet(pet_api):
    logger.info("Starting test: Adding a duplicate pet")

    pet_file = os.path.join(os.path.dirname(__file__), '../../../data/new_pet.json')
    with open(pet_file, 'r') as file:
        new_pet = json.load(file)
    logger.info(f"Loaded pet data from {pet_file}: {new_pet}")

    logger.info("Attempting to add the duplicate pet")
    duplicate_response = pet_api.add_pet(new_pet)
    logger.info(f"Response status code for first addition: {duplicate_response.status_code}")
    assert duplicate_response.status_code == 200, f"Expected 200 OK, but got {duplicate_response.status_code}"

    logger.info(f"Fetching the pet with ID: {new_pet['id']}")
    fetched_pet = pet_api.get_pet(new_pet["id"]).json()
    logger.info(f"Fetched pet data: {fetched_pet}")

    assert fetched_pet["name"] == new_pet["name"], f"Expected name to be {new_pet['name']}, but got {fetched_pet['name']}"
    logger.info(f"Pet name is '{fetched_pet['name']}' as expected")