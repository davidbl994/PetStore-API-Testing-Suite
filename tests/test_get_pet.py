from utils.logger import get_logger

logger = get_logger()

def test_get_pet(pet_api, pet_data):
    pet_id = pet_data['id']
    expected_name = pet_data['name']

    logger.info(f"Fetching pet with ID: {pet_id}")
    response = pet_api.get_pet(pet_id)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    logger.info("Status code is 200 as expected")

    pet_data = response.json()
    assert "name" in pet_data, "Response JSON does not contain 'name'"
    assert pet_data["name"] == expected_name, f"Expected pet name to be '{expected_name}', got {pet_data['name']}"
    logger.info(f"Pet name is '{expected_name}' as expected")

def test_get_non_existent_pet(pet_api, non_existent_id):
    pet_id = non_existent_id["id"]

    logger.info(f"Attempting to fetch pet with non-existent ID: {pet_id}")
    response = pet_api.get_pet(pet_id)

    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    logger.info("Status code is 404 as expected")

    response_json = response.json()
    assert "message" in response_json, "Response JSON does not contain 'message'"
    assert response_json["message"] == "Pet not found", f"Expected message 'Pet not found', got {response_json.get('message')}"
    logger.info("Response message 'Pet not found' as expected")

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