import os
import sys
import json
import requests
from spotius.spotus import spotus
from speedtest_demo import speedtesting
from tr import translateit
from wiki import wikipy
from typo import typos
from gh import gith

import rich
from rich import pretty
from rich.console import Console

console = Console()

spotius = spotus()
speedtest = speedtesting()
translated = translateit()
wiki = wikipy()
typoz = typos()
github = gith()

class omeniscient():

    def __init__(self):
        os.system("clear")
        self.start()

    def start(self):

        while True:

            try:

                user_input = input("1337$ ")
                user_command = user_input.split()[0].lower()


                if user_command == "lyrics":

                    spotius.lyrics(user_input.split()[1], user_input.split()[2])

                elif user_command == "lyricsnow":

                    spotius.currently_playing_lyrics()

                elif user_command == "downloadspeed":

                    speedtest.get_download_speed()

                elif user_command == "uploadspeed":

                    speedtest.get_upload_speed()

                elif user_command == "internet":

                    speedtest.get_all_speed()

                elif user_command == "aztr":

                    console.print(
                        f'{requests.get(f"https://azleks-api.herokuapp.com/{user_input.split()[1]}").json()[user_input.split()[1]]}',
                        style="green")

                elif user_command == "en":

                    translated.entr(user_input[2:])

                elif user_command == "tr":

                    translated.trtr(user_input[2:])

                elif user_command == "de":

                    translated.detr(user_input[2:])

                elif user_command == "fr":

                    translated.frtr(user_input[2:])

                elif user_command == "clear":

                    os.system("clear")

                elif user_command == "suggest":

                    wiki.suggesting(user_input[8:])

                elif user_command == "summary":

                    wiki.summarizing(user_input[8:])

                elif user_command == "typo":

                    typoz.check(user_input[4:])

                elif user_command == "gh":

                    github.get_info(user_input[3:])

            except:

                console.print("An error has occurred!", style="red")
                return "An error has occurred!"
