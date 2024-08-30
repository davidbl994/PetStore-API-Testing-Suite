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

    # Verify updated pet details
    logger.info(f"Fetching updated pet details for ID: {pet_id}")
    updated_response = pet_api.get_pet(pet_id)

    assert updated_response.status_code == 200, f"Expected status code 200, but got {updated_response.status_code}"
    updated_pet_data = updated_response.json()

    assert updated_pet_data['name'] == "Updated Name", f"Expected name to be 'Updated Name', got {updated_pet_data['name']}"
    assert updated_pet_data['status'] == "sold", f"Expected status to be sold, got {updated_pet_data['status']}"
    logger.info("Pet details updated successfully via POST")

def test_update_non_existent_pet(pet_api, non_existent_pet_data):
    logger.info(f"Attempting to update a non-existent pet with ID: {non_existent_pet_data['id']}")

    response = pet_api.update_pet(non_existent_pet_data)
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    logger.info("Status code is 404 as expected")

    response_json = response.json()
    assert "message" in response_json, "Response JSON does not contain 'message'"
    assert response_json["message"] == "Pet not found", f"Expected message 'Pet not found', got {response_json.get('message')}"
    logger.info("Received expected 'Pet not found' message")