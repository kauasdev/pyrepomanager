import os
import requests

try:
    user_gh = input("GitHub username: ").strip().lower()
    repos = requests.get(f"https://api.github.com/users/{user_gh}/repos")
    if repos.status_code == 200:
        os.system("gh auth refresh -h github.com -s delete_repo")
        for repo in repos.json():
            r_name = repo['name']
            confirm_del = input(f"Do you want to delete the '{r_name}' repository?(Y/N) ").strip().upper()
            if confirm_del == "Y":
                os.system(f"gh repo delete {r_name} --confirm")
            else:
                continue
    else:
        print("User not found!")
except Exception as error:
    print(error)
