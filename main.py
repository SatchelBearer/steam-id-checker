# Import the necessary modules
import requests
import json

# Define a function that takes a Steam account name and checks if it is available
def check_steam_account_name(account_name):
    # Construct the URL for the Steam API call
    url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
    params = {"key": "YOUR_STEAM_API_KEY", "vanityurl": account_name}

    # Make the API call and get the response
    response = requests.get(url, params=params)
    data = json.loads(response.text)

    # Check the response and return the result
    if "response" in data and "success" in data["response"] and data["response"]["success"] == 1:
        return False
    else:
        return True

# Open the file containing the Steam account names to check
with open("account_names.txt", "r") as f:
    # Read the account names from the file
    account_names = f.readlines()

    # Loop through the account names and check if they are available
    for account_name in account_names:
        # Strip the newline character from the account name
        account_name = account_name.strip()

        # Check if the account name is available
        if check_steam_account_name(account_name):
            print(account_name + " is available")
        else:
            print(account_name + " is not available")