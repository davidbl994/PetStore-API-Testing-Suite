import pytest
from utils.logger import get_logger
logger = get_logger()

def test_delete_order_by_id(store_api, place_order):
    store_id = place_order['id']

    delete_store = store_api.delete_store_order(store_id)
    assert delete_store.status_code == 200, f"Expected status code 200, got {delete_store.status_code}"
    logger.info("Store deleted successfully")

    get_deleted_store = store_api.get_order(store_id)
    assert get_deleted_store.status_code == 404, f"Expected status code 404, got {get_deleted_store.status_code}"
    logger.info("Verified pet is deleted as expected")