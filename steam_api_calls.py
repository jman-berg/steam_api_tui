from dotenv import load_dotenv
import os
import requests

load_dotenv()
steam_id = os.getenv("STEAM_ID")
steam_api_key = os.getenv("STEAM_API_KEY")

response = requests.get()
