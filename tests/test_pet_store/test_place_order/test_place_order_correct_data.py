import json
import os
from utils.logger import get_logger

logger = get_logger()

def test_place_order_correct_data(store_api):
    logger.info("Starting test: Placing an order")

    store_file = os.path.join(os.path.dirname(__file__), '../../../data/order_data.json')
    with open(store_file, 'r') as file:
        new_order = json.load(file)
    logger.info(f"Loaded store data from {store_file}: {new_order}")

    response = store_api.add_order(new_order)
    logger.info(f"Received response with status code: {response.status_code}")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    logger.info("Status code is 200 as expected")

    order_status = response.json().get("status")
    assert order_status == "placed", f"Expected order status to be 'placed' got {order_status}"
    logger.info(f"Order status is '{order_status}' as expected")
