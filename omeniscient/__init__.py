import os
import sys
import json
import requests
from spotius.spotus import spotus
from speedtest_demo import speedtesting
from tr import translateit
from wiki import wikipy

import rich
from rich import pretty
from rich.console import Console

console = Console()

spotius = spotus()
speedtest = speedtesting()
translated = translateit()
wiki = wikipy()


class omeniscient():

    def __init__(self):
        self.start()

    def start(self):

        while True:

            try:

                user_input = input("1337$ ")

                if user_input.split()[0].lower() == "lyrics":

                    spotius.lyrics(user_input.split()[1], user_input.split()[2])

                elif user_input.split()[0].lower() == "lyricsnow":

                    spotius.currently_playing_lyrics()

                elif user_input.split()[0].lower() == "downloadspeed":

                    speedtest.get_download_speed()

                elif user_input.split()[0].lower() == "uploadspeed":

                    speedtest.get_upload_speed()

                elif user_input.split()[0].lower() == "internet":

                    speedtest.get_all_speed()

                elif user_input.split()[0].lower() == "aztr":

                    console.print(
                        f'{requests.get(f"https://azleks-api.herokuapp.com/{user_input.split()[1]}").json()[user_input.split()[1]]}',
                        style="green")

                elif user_input.split()[0].lower() == "en":

                    translated.entr(user_input[2:])

                elif user_input.split()[0].lower() == "tr":

                    translated.trtr(user_input[2:])

                elif user_input.split()[0].lower() == "de":

                    translated.detr(user_input[2:])

                elif user_input.split()[0].lower() == "fr":

                    translated.frtr(user_input[2:])

                elif user_input.split()[0].lower() == "clear":

                    os.system("clear")

                elif user_input.split()[0].lower() == "suggest":

                    wiki.suggesting(user_input[8:])

                elif user_input.split()[0].lower() == "summary":

                    wiki.summarizing(user_input[8:])

            except:

                console.print("An error has occurred!", style="red")
                return "An error has occurred!"
