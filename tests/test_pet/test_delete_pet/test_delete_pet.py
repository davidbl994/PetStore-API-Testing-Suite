import pytest
from utils.logger import get_logger
logger = get_logger()

@pytest.fixture
def pet_data():
    return {
        "id": 99999,
        "name": "Rex",
        "photoUrls": ["https://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "dog"}],
        "status": "available"
    }

def test_delete_pet(pet_api, pet_data):
    pet_id = pet_data['id']

    # First, add the pet
    add_response = pet_api.add_pet(pet_data)
    assert add_response.status_code == 200, "Failed to add pet before deletion"

    logger.info(f"Deleting pet with ID: {pet_id}")

    # Now delete the pet
    delete_response = pet_api.delete_pet(pet_id)
    assert delete_response.status_code == 200, f"Expected status code 200, got {delete_response.status_code}"
    logger.info("Pet deleted successfully")

    # Try to get the deleted pet
    get_response = pet_api.get_pet(pet_id)
    assert get_response.status_code == 404, f"Expected status code 404, got {get_response.status_code}"
    logger.info("Verified pet is deleted as expected")