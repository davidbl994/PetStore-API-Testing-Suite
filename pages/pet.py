import requests
import logging

class Pet:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    def add_pet(self, pet_data):
        url = f"{self.base_url}/pet"
        self.logger.info(f"Sending POST request to {url} with data: {pet_data}")
        response = requests.post(url, json=pet_data)
        self.logger.info(f"Received response: {response.status_code} - {response.json()}")
        return response

    def get_pet(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(url)
        self.logger.info(f"Received response: {response.status_code} - {response.json()}")
        return response

    def delete_pet(self, pet_id):
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.delete(url)
        return response