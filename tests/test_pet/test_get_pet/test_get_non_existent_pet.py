from utils.logger import get_logger

logger = get_logger()

def test_get_non_existent_pet(pet_api, non_existent_id):
    pet_id = non_existent_id['id']

    logger.info(f"Attempting to fetch pet with non-existent ID: {pet_id}")
    response = pet_api.get_pet(pet_id)

    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    logger.info("Status code is 404 as expected")

    response_json = response.json()
    assert "message" in response_json, "Response JSON does not contain 'message'"
    assert response_json["message"] == "Pet not found", f"Expected message 'Pet not found', got {response_json.get('message')}"
    logger.info("Response message 'Pet not found' as expected")