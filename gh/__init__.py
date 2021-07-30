import requests
import json

import rich
from rich import pretty
from rich.console import Console

console = Console()

class gith():
    def __init__(self):
        pass

    def get_info(self, username):

        """
        Gets a username on GitHub as an argument, gets the information regarding that person on GitHub
        :param username:
        :return:
        """

        try:

            user = requests.get(f"https://api.github.com/users/{username}").json()

            console.print(f'ID: {user["id"]}',style="green")
            console.print(f'Avatar URL: {user["avatar_url"]}',style="green")
            console.print(f'Name: {user["name"]}',style="green")
            console.print(f'Companies: {user["company"]}', style="green")
            console.print(f'Blog: {user["blog"]}', style="green")
            console.print(f'Location: {user["location"]}', style="green")
            console.print(f'Email: {user["email"]}', style="green")
            console.print(f'Bio: {user["bio"]}', style="green")
            console.print(f'Public Repos: {user["public_repos"]}', style="green")
            console.print(f'Public Gists: {user["public_gists"]}', style="green")
            console.print(f'Followers: {user["followers"]}', style="green")
            console.print(f'Following: {user["following"]}', style="green")

            return True

        except:

            console.print("An Error has Occurred in GitHub Requests")

            return False