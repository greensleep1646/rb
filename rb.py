import requests

def get_user_info(username):
    url = f"https://api.roblox.com/users/get-by-username?username={username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        if "Id" in user_data:
            user_id = user_data["Id"]
            print(f"Username: {username}")
            print(f"User ID: {user_id}")
            print(f"Profile Link: https://www.roblox.com/users/{user_id}/profile")
        else:
            print("User not found.")
    else:
        print("An error occurred while retrieving user information.")

# Usage
username = input("Enter the Roblox username: ")
get_user_info(username)
