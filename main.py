from steam_api_calls import steam_api 
from environment_variables import id_and_key_check


def main ():
    id_and_key_check()
    steam_api.get_owned_games()

if __name__ == "__main__":
    main()
