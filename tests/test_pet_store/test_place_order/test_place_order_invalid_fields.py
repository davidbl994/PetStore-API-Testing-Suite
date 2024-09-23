import json
import os
from utils.logger import get_logger

logger = get_logger()

def test_place_order_invalid_data(store_api):
    logger.info("Starting test: Placing an order with invalid fields")

    store_file = os.path.join(os.path.dirname(__file__), '../../../data/order_data_invalid_fields.json')
    with open(store_file, 'r') as file:
        invalid_order = json.load(file)
    logger.info(f"Loaded store data from {store_file}: {invalid_order}")

    response = store_api.add_order(invalid_order)
    logger.info(f"Received response with status code {response.status_code}")

    assert response.status_code == 500, f"Expected status code 500, got {response.status_code}"
    logger.info("Status code is 500 as expected")

    error_message = response.json().get("message")
    logger.info(f"Error message: {error_message}")