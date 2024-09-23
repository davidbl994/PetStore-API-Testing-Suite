from utils.logger import get_logger

logger = get_logger()

def test_delete_non_existent_store(store_api, non_existent_id):
    store_id = non_existent_id['id']
    logger.info(f"Attempting to delete a non-existent store with ID: {store_id}")

    response = store_api.delete_store_order(store_id)

    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"
    logger.info("Status code is 404 as expected")

    if response.content:
        response_json = response.json()
        assert "message" in response_json, "Response JSON does not contain 'message'"
        assert response_json["message"] == "Order Not Found", f"Expected message 'Store not found', got {response_json.get('message')}"
        logger.info("Received expected 'Order Not Found' message")
    else:
        logger.info("No response body received, as expected for a 404 error")