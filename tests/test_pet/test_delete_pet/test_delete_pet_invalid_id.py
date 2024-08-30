import pytest
from utils.logger import get_logger

logger = get_logger()

def test_delete_pet_invalid_id(pet_api, invalid_pet_data):
    pet_id = invalid_pet_data['id']
    logger.info(f"Attempting to delete pet with invalid ID format: {pet_id}")

    response = pet_api.delete_pet(pet_id)

    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    logger.info("Status code is 404 as expected")

    if response.content:
        response_json = response.json()
        assert "message" in response_json, "Response JSON does not contain 'message'"
        assert "NumberFormatException" in response_json[
            "message"], f"Unexpected message: {response_json.get('message')}"
        logger.info("Received expected 'NumberFormatException' in the message")
    else:
        logger.warning("No response body received when an invalid ID format was used")