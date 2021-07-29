from dotenv import load_dotenv
import os
load_dotenv()

import json
import spotipy
import lyricsgenius as lg

spotifyOAuth = spotipy.SpotifyOAuth(client_id=os.environ['SPOTIPY_CLIENT_ID'],
                                    client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
                                    redirect_uri=os.environ['SPOTIPY_REDIRECT_URL'],
                                    scope="user-read-currently-playing")

token_dict = spotifyOAuth.get_access_token()
spotify_access_token = token_dict["access_token"]

spotify_object = spotipy.Spotify(auth=spotify_access_token)
currently_playing = spotify_object.currently_playing()
#print(json.dumps(currently_playing, sort_keys=True, indent=4))

# Track type condition check
if currently_playing["item"]["type"] == "track":
    artist_name = currently_playing["item"]["album"]["artists"][0]["name"]
    song_name = currently_playing["item"]["name"]
    print(artist_name, " ", song_name)


# Genius
genius_obj = lg.Genius(os.getenv("GENIUS_ACCESS_TOKEN"))
song =  genius_obj.search_song(title=song_name, artist=artist_name)
lyrics = song.lyrics

print(lyrics)