from utils.logger import get_logger

logger = get_logger()

def test_get_pet_invalid_id(pet_api, invalid_pet_data):
    pet_id = invalid_pet_data['id']

    logger.info(f"Attempting to fetch pet with invalid ID format: {pet_id}")
    response = pet_api.get_pet(pet_id)

    assert response.status_code == 404, f"Expected status code 400, got {response.status_code}"
    logger.info("Status code is 400 as expected")

    response_json = response.json()
    assert "message" in response_json, "Response JSON does not contain 'message'"
    assert response_json["message"] == f'java.lang.NumberFormatException: For input string: "{pet_id}"', \
        f"Expected message 'java.lang.NumberFormatException: For input string: \"{pet_id}\"', got {response_json.get('message')}"
    logger.info(f"Response message '{response_json['message']}' as expected")