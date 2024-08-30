from utils.logger import get_logger

logger = get_logger()

def test_get_pet(pet_api, pet_data):
    pet_id = pet_data['id']
    expected_name = pet_data['name']

    logger.info(f"Fetching pet with ID: {pet_id}")

    try:
        response = pet_api.get_pet(pet_id)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        logger.info("Status code is 200 as expected")

        pet_data = response.json()
        assert "name" in pet_data, "Response JSON does not contain 'name'"
        assert pet_data["name"] == expected_name, f"Expected pet name to be '{expected_name}', got {pet_data['name']}"
        logger.info(f"Pet name is '{expected_name}' as expected")
    except AssertionError as e:
        logger.error(f"Test failed: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise