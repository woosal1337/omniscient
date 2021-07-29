import os
import sys
import json
import requests
from spotius.spotus import spotus
from speedtest_demo import speedtesting
from tr import translateit

import rich
from rich import pretty
from rich.console import Console

console = Console()

spotius = spotus()
speedtest = speedtesting()
translated = translateit()

class omeniscient():

    def __init__(self):
        self.start()

    def start(self):

        while True:

            try:

                user_input = input("1337$ ")

                if user_input.split()[0] == "lyrics":

                    spotius.lyrics(user_input.split()[1], user_input.split()[2])

                elif user_input.split()[0] == "lyricsnow":

                    spotius.currently_playing_lyrics()

                elif user_input.split()[0] == "downloadspeed":

                    speedtest.get_download_speed()

                elif user_input.split()[0] == "uploadspeed":

                    speedtest.get_upload_speed()

                elif user_input.split()[0] == "internet":

                    speedtest.get_all_speed()

                elif user_input.split()[0] == "aztr":

                    console.print(f'{requests.get(f"https://azleks-api.herokuapp.com/{user_input.split()[1]}").json()[user_input.split()[1]]}', style="green")

                elif user_input.split()[0] == "en":

                    translated.entr(user_input[2:])

                elif user_input.split()[0] == "tr":

                    translated.trtr(user_input[2:])

                elif user_input.split()[0] == "de":

                    translated.detr(user_input[2:])

                elif user_input.split()[0] == "fr":

                    translated.frtr(user_input[2:])

                elif user_input.split()[0] == "clear":

                    os.system("clear")

            except:

                console.print("An error has occurred!", style="red")
                return "An error has occurred!"