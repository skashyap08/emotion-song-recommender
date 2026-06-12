import pandas as pd
import random
import webbrowser

opened = False

def recommend_song(emotion):

    df = pd.read_csv("songs.csv")

    songs = df[df["emotion"] == emotion]

    if songs.empty:
        return None

    selected = songs.sample(1).iloc[0]

    return {
        "song": selected["song"],
        "artist": selected["artist"],
        "link": selected["spotify_link"]
    }

def open_spotify(link):
    global opened

    if not opened:
        webbrowser.open(link)
        opened = True