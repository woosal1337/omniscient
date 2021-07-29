import os
import sys
import rich
import json
import requests
from spotius.spotus import spotus
from speedtest_demo import speedtesting

spotius = spotus()
speedtest = speedtesting()

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

                    print(requests.get(f"https://azleks-api.herokuapp.com/{user_input.split()[1]}").json()[user_input.split()[1]])

            except:

                print("An error has occurred!")
                return "An error has occurred!"