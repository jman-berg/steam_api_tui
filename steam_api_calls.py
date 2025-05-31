from dotenv import load_dotenv
import os
import requests
from theme import console


load_dotenv()
steam_id = os.getenv("STEAM_ID")
steam_api_key = os.getenv("STEAM_API_KEY")


base_url = "http://api.steampowered.com/"


# Services 
player_service = "IPlayerService/" 

# Calls

get_owned_games = "GetOwnedGames/v0001/"



class SteamApi:
    def __init__(self, key, steamid):
        self.params = {"key": key, "steamid" : steamid}


    def get_owned_games(self):
        response = requests.get(f"{base_url}{player_service}{get_owned_games}", params=self.params)
        print(response.json()['response']['game_count'])

    def get_user_profile(self):
        response = requests.get()

steam_api = SteamApi(key=steam_api_key, steamid=steam_id)


 

        

