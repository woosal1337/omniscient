"""
Author: @woosal1337
"""

from dotenv import load_dotenv
import os

load_dotenv()

import json
import spotipy
import lyricsgenius as lg
import time

class spotus():
    def __init__(self):
        self.setup()

    def setup(self) -> str:

        """
        Load .env Tokens, IDs, and Secrets to the Auth
        :return:
        """

        try:

            self.spotifyOAuth = spotipy.SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                                     client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                                     redirect_uri=os.environ['SPOTIPY_REDIRECT_URL'],
                                                     scope="user-read-currently-playing")

            self.token_dict = self.spotifyOAuth.get_access_token()
            self.spotify_access_token = self.token_dict["access_token"]

            spotify_object = spotipy.Spotify(auth=self.spotify_access_token)
            self.genius_obj = lg.Genius(os.getenv("GENIUS_ACCESS_TOKEN"))

            self.currently_playing = spotify_object.currently_playing()
            # print(json.dumps(currently_playing, sort_keys=True, indent=4))

        except:

            print("An error occurred in the setup!")
            return "An error occurred in the setup!"

    def update_currently_playing(self) -> str:

        """
        Fetch the latest currently playing list and return the .json
        :return: json:str of the current playing song&artist details
        """

        try:
            spotify_object = spotipy.Spotify(auth=self.spotify_access_token)
            self.currently_playing = spotify_object.currently_playing()

            if self.currently_playing["item"]["type"] == "track":
                self.artist_name = self.currently_playing["item"]["album"]["artists"][0]["name"]
                self.song_name = self.currently_playing["item"]["name"]

            return self.currently_playing

        except:
            print("An error occurred while fetching the song name & artist name.")
            return "An error occurred while fetching the song name & artist name."

    def currently_playing_songname_artistname(self) -> str:

        """
        Fetch the live user Spotify account and return the track name & the artist name
        :return: song_name:str, artist_name:str
        """

        try:

            self.update_currently_playing()

            if self.currently_playing["item"]["type"] == "track":
                self.artist_name = self.currently_playing["item"]["album"]["artists"][0]["name"]
                self.song_name = self.currently_playing["item"]["name"]
                print(f"Song: {self.song_name}\nArtist: {self.artist_name}")
                return (self.artist_name, self.song_name)

        except:

            print(
                "An error occurred while fetching the song name & artist name! Please listen to a `track` type of music to get the lyrics.")
            return "An error occurred while fetching the song name & artist name! Please listen to a `track` type of music to get the lyrics."

    def currently_playing_lyrics(self):

        """
        Take artist&song names and return lyrics of the track through Genius API
        :param artist_name:
        :param song_name:
        :return:
        """

        try:
            self.update_currently_playing()

            song = self.genius_obj.search_song(title=self.song_name, artist=self.artist_name)
            self.lyrics = song.lyrics

            print(self.lyrics)
            return self.lyrics

        except:
            print("An error occurred while fetching the lyrics!")
            return "An error occurred while fetching the lyrics!"

    def lyrics(self, song_name:str, artist_name = None):

        """
        Take artist&song names and return lyrics of the track through Genius API
        :param artist_name:
        :param song_name:
        :return:
        """

        try:

            if artist_name:

                song = self.genius_obj.search_song(title=song_name, artist=artist_name)
                self.lyrics = song.lyrics

                print(self.lyrics)
                return self.lyrics

            else:

                song = self.genius_obj.search_song(title=song_name)
                self.lyrics = song.lyrics

                print(self.lyrics)
                return self.lyrics

        except:
            print("An error occurred while fetching the lyrics!")
            return "An error occurred while fetching the lyrics!"
