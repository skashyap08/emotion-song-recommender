import pandas as pd
import random
import webbrowser

def recommend_song(emotion):

    df = pd.read_csv("songs.csv")

    songs = df[df["emotion"] == emotion]

    if songs.empty:
        return None

    selected = songs.sample(1).iloc[0]

    return {
        "song": selected["song"],
        "link": selected["spotify_link"]
    }

def open_song(link):
    webbrowser.open(link)