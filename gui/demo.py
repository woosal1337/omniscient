import os
import sys
import rich
import json
from spotius.spotus import spotus

spotius = spotus()

class omeniscient():
    def __init__(self):
        self.start()

    def start(self):

        while True:

            try:

                user_input = input("$ ")

                if user_input.split()[0] == "lyrics":

                    spotius.lyrics(user_input.split()[1], user_input.split()[2])

                elif user_input.split()[0] == "lyricsnow":

                    spotius.currently_playing_lyrics()

                elif user_input.split()[0] == "translateaz":

                    pass

            except:

                print("An error has occurred!")
                return "An error has occurred!"

demo = omeniscient()