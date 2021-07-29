from dotenv import load_dotenv
import os
load_dotenv()

import json
import spotipy
import lyricsgenius as lg

# Genius
genius_obj = lg.Genius(os.getenv("GENIUS_ACCESS_TOKEN"))
song =  genius_obj.search_song(title="CASINO ROYAL")
lyrics = song.lyrics

print(lyrics)