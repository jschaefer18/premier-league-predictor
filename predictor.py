import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file
api_key = os.getenv("API_FOOTBALL_KEY")
print(api_key)  # test