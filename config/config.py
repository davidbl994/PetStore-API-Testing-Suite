import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('PET_STORE_API_KEY')
BASE_URL = "https://petstore.swagger.io/v2"