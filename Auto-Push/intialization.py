import json
import getpass

repo_exists = input('Do you already have an existing repo for leetcode solutions (y/n): ')
if repo_exists.lower() == 'n':
    print("Disclaimer, creating a new PAT solely for the use of this script is highly recommended")
    git_pat = getpass.getpass("Enter your GitHub Personal Access Token (PAT): ")
    repo_name = input("Enter the name you would like for t")


# repo_url = input("Enter your repository URL: ")
username = input('Enter your GitHub username: ')
session_id = getpass.getpass('Enter your leetcode session ID: ')

user_info = {
    "username": username,
    "session_id": session_id
}

with open("user_info.json", "w") as f:
    json.dump(user_info, f, indent=2)

print('User info is saved to user_info.json')


