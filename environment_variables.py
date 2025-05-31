from dotenv import load_dotenv
import os
from rich import print 
from rich.panel import Panel
from theme import console

load_dotenv()


def id_and_key_check():
    steam_id = os.getenv("STEAM_ID")
    steam_api_key = os.getenv("STEAM_API_KEY")
    if steam_id and steam_api_key:
        pass
    else:
        console.print(Panel("Welcome to the Steam TUI! I didn't find a set [bold]steam ID[/bold] or [bold]steam api key[/bold]. Would you like to set those? You can request a steam api key [link=https://steamcommunity.com/dev/apikey]here.[/link]", title="INITIAL SET UP", border_style = "accent", style="foreground"))
        steam_api_key = input("Steam Api Key: ")
        steam_id = input("Steam ID: ")
        with open(".env", "w") as env:
            env.writelines([f"STEAM_API_KEY={steam_api_key}","\n",f"STEAM_ID={steam_id}"])
    return steam_id, steam_api_key
    
id_and_key_check()
