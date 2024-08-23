import json
from utils.logger import get_logger

logger = get_logger()

def test_update_pet_details(pet_api, pet_data):
    pet_id = pet_data['id']

    # Fetch existing pet details
    logger.info(f"Fetching pet with ID: {pet_id}")
    response = pet_api.get_pet(pet_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
