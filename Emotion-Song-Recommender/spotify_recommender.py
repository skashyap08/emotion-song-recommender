import pandas as pd
import random

def recommend_song(emotion):
    df = pd.read_csv("songs.csv")

    songs = df[df['emotion'] == emotion]['song'].tolist()

    if songs:
        return random.choice(songs)
    else:
        return "No song found"