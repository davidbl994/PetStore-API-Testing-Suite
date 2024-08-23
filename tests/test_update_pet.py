import json
from utils.logger import get_logger

logger = get_logger()

def test_update_pet_details(pet_api, pet_data):
    pet_id = pet_data['id']

    # Fetch existing pet details
    logger.info(f"Fetching pet with ID: {pet_id}")
    response = pet_api.get_pet(pet_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    pet_info = response.json()

    updated_pet_info = pet_info.copy()
    updated_pet_info['name'] = "Updated Name"
    updated_pet_info['status'] = "sold"

    logger.info(f"Updating pet with ID: {pet_id} using POST request")
    post_response = pet_api.add_pet(updated_pet_info)

    assert post_response.status_code == 200, f"Expected status code 200, but got {post_response.status_code}"
    logger.info("Update via POST successful")