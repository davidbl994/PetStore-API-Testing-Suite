import json
import os
from utils.logger import get_logger

logger = get_logger()

def test_add_pet_missing_field(pet_api):
    logger.info("Starting test: Adding a pet with a missing field")

    pet_file = os.path.join(os.path.dirname(__file__), '../../../data/new_pet_missing_field.json')
    with open(pet_file, 'r') as file:
        pet_missing_filed = json.load(file)
    logger.info(f"Loaded pet data with missing field from {pet_file}: {pet_missing_filed}")

    response = pet_api.add_pet(pet_missing_filed)
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response content: {response.json()}")

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    logger.info("Status code is 200 as expected")

    assert response.json()["status"] == "xoxo", "Expected status to be 'xoxo'"
    logger.info("Pet status is 'xoxo' as expected")